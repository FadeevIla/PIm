from sqlalchemy import text
from db import get_engine

def create_tables():
    """Создаёт таблицы в PostgreSQL с NDS и DDS."""

    create_tables_sql = text("""
    -- Удаление старых таблиц
    DROP TABLE IF EXISTS fact_sales CASCADE;
    DROP TABLE IF EXISTS dim_stores CASCADE;
    DROP TABLE IF EXISTS dim_time CASCADE;
    DROP TABLE IF EXISTS dim_products CASCADE;
    DROP TABLE IF EXISTS dim_customers CASCADE;
    DROP TABLE IF EXISTS nds_sales CASCADE;

    -- Таблица NDS (нормализованные данные)
    CREATE TABLE nds_sales (
        invoice_id VARCHAR(20) PRIMARY KEY,
        branch VARCHAR(1),
        city VARCHAR(50),
        customer_type VARCHAR(20),
        gender VARCHAR(10),
        product_line VARCHAR(100),
        unit_price NUMERIC(10,2),
        quantity INT,
        tax NUMERIC(10,2),
        total NUMERIC(10,2),
        payment_method VARCHAR(20),
        cogs NUMERIC(10,2),
        gross_margin_percentage NUMERIC(10,6),
        gross_income NUMERIC(10,2),
        rating NUMERIC(3,1),
        date DATE,
        time TIME
    );

    -- Таблицы DDS (денормализация)
    CREATE TABLE dim_stores (
        store_id SERIAL PRIMARY KEY,
        branch VARCHAR(1) NOT NULL,
        city VARCHAR(50) NOT NULL
    );

    CREATE TABLE dim_time (
        time_id SERIAL PRIMARY KEY,
        date DATE NOT NULL,
        time TIME NOT NULL,
        day_of_week VARCHAR(10) NOT NULL,
        month INT NOT NULL,
        year INT NOT NULL
    );

    CREATE TABLE dim_products (
        product_id SERIAL PRIMARY KEY,
        product_line VARCHAR(100) NOT NULL
    );

    CREATE TABLE dim_customers (
        customer_id SERIAL PRIMARY KEY,
        customer_type VARCHAR(20) NOT NULL
    );

    CREATE TABLE fact_sales (
        sale_id SERIAL PRIMARY KEY,
        invoice_id VARCHAR(20) NOT NULL,
        store_id INT REFERENCES dim_stores(store_id),
        time_id INT REFERENCES dim_time(time_id),
        product_id INT REFERENCES dim_products(product_id),
        customer_id INT REFERENCES dim_customers(customer_id),
        gender VARCHAR(10) NOT NULL,
        unit_price NUMERIC(10,2) NOT NULL,
        quantity INT NOT NULL,
        tax NUMERIC(10,2) NOT NULL,
        total NUMERIC(10,2) NOT NULL,
        payment_method VARCHAR(20) NOT NULL,
        cogs NUMERIC(10,2) NOT NULL,
        gross_margin_percentage NUMERIC(10,6) NOT NULL,
        gross_income NUMERIC(10,2) NOT NULL,
        rating NUMERIC(3,1) NOT NULL
    );
    """)

    engine = get_engine()
    with engine.connect() as conn:
        conn.execute(create_tables_sql)
        conn.commit()
    print("Таблицы NDS и DDS успешно созданы!")


def load_data(nds_df, dim_stores, dim_time, dim_products, dim_customers, fact_sales):
    """Загружает данные в PostgreSQL."""
    engine = get_engine()
    print(nds_df.dtypes)
    # Сначала загружаем NDS
    nds_df.to_sql("nds_sales", engine, if_exists="append", index=False)

    # Затем DDS
    dim_stores.to_sql("dim_stores", engine, if_exists="append", index=False)
    dim_time.to_sql("dim_time", engine, if_exists="append", index=False)
    dim_products.to_sql("dim_products", engine, if_exists="append", index=False)
    dim_customers.to_sql("dim_customers", engine, if_exists="append", index=False)
    fact_sales.to_sql("fact_sales", engine, if_exists="append", index=False)

    print("Данные загружены в NDS и DDS!")
