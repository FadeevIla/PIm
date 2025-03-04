import pandas as pd
from ydata_profiling import ProfileReport

def generate_eda_report(csv_file: str, output_file: str = "eda_report.html"):
    """
    Генерирует EDA-отчет на основе входного CSV-файла.

    :param csv_file: Путь к CSV-файлу с данными.
    :param output_file: Название выходного HTML-файла с отчетом.
    """
    print(f"Читаем данные из {csv_file}...")
    df = pd.read_csv(csv_file)

    print("Генерируем отчет YData Profiling...")
    profile = ProfileReport(df, explorative=True)

    print(f"Сохраняем отчет в {output_file}")
    profile.to_file(output_file)

    print("EDA-отчет успешно создан!")

if __name__ == "__main__":
    generate_eda_report("supermarket_sales.csv")
