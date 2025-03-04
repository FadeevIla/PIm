import pandas as pd

def extract_data(file_path):
    """Считывает CSV без изменений (ODS-слой)."""
    df = pd.read_csv(file_path)

    print("Данные загружены в ODS (сырые данные).")
    return df
