import pandas as pd


def check_missing_values(df):
    """Проверяет, есть ли в данных пропущенные значения."""
    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0]
    if not missing_values.empty:
        print("Найдены пропущенные значения:")
        print(missing_values)
    else:
        print("Пропущенных значений нет.")


def check_duplicates(df):
    """Проверяет наличие дубликатов по ключевым колонкам."""
    duplicate_rows = df[df.duplicated(subset=["invoice_id"], keep=False)]
    if not duplicate_rows.empty:
        print(f"Найдено {len(duplicate_rows)} дубликатов по 'invoice_id'.")
    else:
        print("Дубликатов нет.")


def check_anomalies(df):
    """Проверяет наличие аномальных значений в числовых колонках."""
    anomalies = df[
        (df["quantity"] <= 0) |
        (df["unit_price"] <= 0) |
        (df["total"] <= 0) |
        (df["gross_income"] < 0) |
        (df["gross_margin_percentage"] < 0) | (df["gross_margin_percentage"] > 100)
        ]

    if not anomalies.empty:
        print("Найдены аномальные значения:")
        print(anomalies[["invoice_id", "quantity", "unit_price", "total", "gross_income", "gross_margin_percentage"]])
    else:
        print("Аномалий не обнаружено.")


def check_data_quality(df):
    """Запускает все проверки качества данных."""
    print("\nЗапуск проверки качества данных...")
    check_missing_values(df)
    check_duplicates(df)
    check_anomalies(df)
    print("Проверка качества данных завершена!\n")
