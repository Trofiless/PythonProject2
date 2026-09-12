from pathlib import Path

from src.reader import get_transactions_csv, get_transactions_excel

DATA_DIR = Path("data")


def test_get_transactions_csv():

    result = get_transactions_csv(DATA_DIR / "transactions.csv")

    assert isinstance(result, list)

    assert len(result) > 0

    assert isinstance(result[0], dict)


def test_get_transactions_excel():

    result = get_transactions_excel(DATA_DIR / "transactions_excel.xlsx")

    assert isinstance(result, list)

    assert len(result) > 0

    assert isinstance(result[0], dict)
