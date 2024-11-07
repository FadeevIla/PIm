import random
import time
from confluent_kafka import Producer
from avro.schema import parse
from avro.io import DatumWriter, BinaryEncoder
import io
from collections import defaultdict, deque

# Настройки Kafka
KAFKA_BROKER = 'kafka:9094'
PURCHASE_TOPIC = 'purchases'
PRODUCT_TOPIC = 'products'
ALERT_TOPIC = 'alerts'
ALERT_THRESHOLD = 3000
#ALERT_THRESHOLD = 1 # для отладки

# Пути к файлам схем Avro
PURCHASE_SCHEMA_PATH = 'schemas/purchase.avsc'
PRODUCT_SCHEMA_PATH = 'schemas/product.avsc'
ALERT_SCHEMA_PATH = 'schemas/alert.avsc'  # Новая схема для алертов

# Инициализация Producer
producer = Producer({'bootstrap.servers': KAFKA_BROKER})

# Чтение и компиляция схем Avro
with open(PURCHASE_SCHEMA_PATH, 'r') as f:
    purchase_schema = parse(f.read())
with open(PRODUCT_SCHEMA_PATH, 'r') as f:
    product_schema = parse(f.read())
with open(ALERT_SCHEMA_PATH, 'r') as f:
    alert_schema = parse(f.read())  # Загружаем схему для алертов

# Хранилище для цен и продаж продуктов
product_prices = {}
product_sales = defaultdict(lambda: deque())

# Функция для сериализации данных в формат Avro
def serialize_avro(data, schema):
    writer = DatumWriter(schema)
    bytes_writer = io.BytesIO()
    encoder = BinaryEncoder(bytes_writer)
    writer.write(data, encoder)
    return bytes_writer.getvalue()

# Функция для генерации сообщения о покупке
def generate_purchase():
    purchase = {
        "id": int(time.time() * 1000),
        "quantity": random.randint(1, 11),
        "productid": random.randint(0, 100)
    }
    avro_data = serialize_avro(purchase, purchase_schema)
    producer.produce(PURCHASE_TOPIC, key=str(purchase["id"]), value=avro_data)
    print(f"Produced purchase: {purchase}")
    process_purchase(purchase)

# Функция для генерации сообщения о продукте
def generate_product():
    product = {
        "id": random.randint(0, 100),
        "name": f"Product-{random.randint(1, 100)}",
        "description": f"Description-{random.randint(1, 100)}",
        "price": round(random.uniform(50, 70), 2)
    }
    avro_data = serialize_avro(product, product_schema)
    producer.produce(PRODUCT_TOPIC, key=str(product["id"]), value=avro_data)
    print(f"Produced product: {product}")
    # Сохраняем цену продукта
    product_prices[product["id"]] = product["price"]

# Функция для обработки покупок и генерации алертов
def process_purchase(purchase):
    product_id = purchase["productid"]
    quantity = purchase["quantity"]
    current_time = time.time()

    # Проверяем, есть ли цена для продукта
    if product_id in product_prices:
        price = product_prices[product_id]
        revenue = quantity * price

        # Удаляем устаревшие покупки
        while product_sales[product_id] and current_time - product_sales[product_id][0][1] > 60:
            product_sales[product_id].popleft()

        # Добавляем текущую покупку
        product_sales[product_id].append((revenue, current_time))

        # Считаем суммарный доход за последние 60 секунд
        total_revenue = sum(sale[0] for sale in product_sales[product_id])

        # Проверяем порог и отправляем алерт
        if total_revenue > ALERT_THRESHOLD:
            alert_message = {
                "product_id": product_id,
                "total_revenue": total_revenue,
                "alert": f"Total revenue for product {product_id} exceeded {ALERT_THRESHOLD} in the last minute!"
            }
            avro_data = serialize_avro(alert_message, alert_schema)
            producer.produce(ALERT_TOPIC, key=str(product_id), value=avro_data)
            print(f"Alert sent: {alert_message}")

# Цикл генерации данных
try:
    while True:
        generate_purchase()
        generate_product()
        producer.flush()
        time.sleep(1)
except KeyboardInterrupt:
    pass
