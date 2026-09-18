import pandas as pd


def get_transactions_csv(file_path: str) -> list[dict]:
    """Считывает финансовые операции из CSV-файла."""

    df = pd.read_csv(file_path, sep=";")

    return df.to_dict(orient="records")


def get_transactions_excel(file_path: str) -> list[dict]:
    """Считывает финансовые операции из Excel-файла."""

    df = pd.read_excel(file_path)

    return df.to_dict(orient="records")
