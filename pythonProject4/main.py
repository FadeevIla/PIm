import random
import time
from confluent_kafka import Producer
from avro.schema import parse
from avro.io import DatumWriter, BinaryEncoder
import io

# Настройки Kafka
KAFKA_BROKER = 'localhost:9093'
PURCHASE_TOPIC = 'purchases'

# Путь к файлу схемы Avro
PURCHASE_SCHEMA_PATH = 'schemas/purchase.avsc'

# Инициализация Producer
producer = Producer({'bootstrap.servers': KAFKA_BROKER})

# Чтение и компиляция схемы Avro
with open(PURCHASE_SCHEMA_PATH, 'r') as f:
    purchase_schema = parse(f.read())

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
        "id": int(time.time() * 1000),             # Используем текущее время в миллисекундах для уникальности
        "quantity": random.randint(1, 11),         # Диапазон от 1 до 11
        "productid": random.randint(0, 100)        # Диапазон от 0 до 100
    }
    avro_data = serialize_avro(purchase, purchase_schema)
    producer.produce(PURCHASE_TOPIC, key=str(purchase["id"]), value=avro_data)
    print(f"Produced purchase: {purchase}")

# Цикл генерации данных
try:
    while True:
        generate_purchase()
        producer.flush()
        time.sleep(1)  # Пауза между сообщениями
except KeyboardInterrupt:
    pass
