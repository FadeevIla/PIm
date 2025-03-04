from etl.extract import extract_data
from etl.transform import normalize_data, transform_data
from etl.load import create_tables, load_data
from data_quality import check_data_quality

FILE_PATH = "supermarket_sales.csv"


def main():
    df = extract_data(FILE_PATH)  # 1. ODS (Сырые данные)

    nds_df = normalize_data(df)  # 2. NDS (Нормализация)

    check_data_quality(nds_df)

    nds_df, dim_stores, dim_time, dim_products, dim_customers, fact_sales = transform_data(nds_df)  # 3. DDS

    create_tables()
    load_data(nds_df, dim_stores, dim_time, dim_products, dim_customers, fact_sales)


if __name__ == "__main__":
    main()
