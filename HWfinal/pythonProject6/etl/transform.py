import pandas as pd

def normalize_data(df):
    """Создаёт нормализованный слой NDS (исправляет названия, форматы данных)."""

    # Приведение типов
    df["date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
    df["time"] = pd.to_datetime(df["Time"], format="%H:%M").dt.time

    # Переименование колонок
    df.rename(columns={
        "Invoice ID": "invoice_id",
        "Branch": "branch",
        "City": "city",
        "Customer type": "customer_type",
        "Gender": "gender",
        "Product line": "product_line",
        "Unit price": "unit_price",
        "Quantity": "quantity",
        "Tax 5%": "tax",
        "Total": "total",
        "Payment": "payment_method",
        "cogs": "cogs",
        "gross margin percentage": "gross_margin_percentage",
        "gross income": "gross_income",
        "Rating": "rating"
    }, inplace=True)
    df = df.drop(columns=["Date"])  # Удаляем дубликат "Date"
    df = df.drop(columns=["Time"])  # Удаляем дубликат "Time"
    print("Данные нормализованы (NDS).")
    return df


def transform_data(nds_df):
    """Создаёт измерения и факт-таблицу из нормализованных данных (NDS)."""

    # Измерение магазинов
    dim_stores = nds_df[["branch", "city"]].drop_duplicates().reset_index(drop=True)
    dim_stores["store_id"] = dim_stores.index + 1

    # Измерение времени
    dim_time = nds_df[["date", "time"]].drop_duplicates().reset_index(drop=True)
    dim_time["day_of_week"] = dim_time["date"].dt.day_name()
    dim_time["month"] = dim_time["date"].dt.month
    dim_time["year"] = dim_time["date"].dt.year
    dim_time["time_id"] = dim_time.index + 1

    # Измерение товаров
    dim_products = nds_df[["product_line"]].drop_duplicates().reset_index(drop=True)
    dim_products["product_id"] = dim_products.index + 1

    # Измерение клиентов
    dim_customers = nds_df[["customer_type"]].drop_duplicates().reset_index(drop=True)
    dim_customers["customer_id"] = dim_customers.index + 1

    # Факт-таблица продаж
    fact_sales = nds_df \
        .merge(dim_stores, on=["branch", "city"], how="left", validate="m:1") \
        .merge(dim_time, on=["date", "time"], how="left", validate="m:1") \
        .merge(dim_products, on=["product_line"], how="left", validate="m:1") \
        .merge(dim_customers, on=["customer_type"], how="left", validate="m:1") \
        [["invoice_id", "store_id", "time_id", "product_id", "customer_id", "gender", "unit_price",
          "quantity", "tax", "total", "payment_method", "cogs", "gross_margin_percentage", "gross_income", "rating"]]

    print("Данные трансформированы в измерения и факт-таблицу.")

    return nds_df, dim_stores, dim_time, dim_products, dim_customers, fact_sales
