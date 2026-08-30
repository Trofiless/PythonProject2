import os
import requests
from dotenv import load_dotenv
from typing import Any

load_dotenv()


def convert_currency(transaction: dict[str, Any]) -> float:
    """Конвертирует сумму транзакции в рубли."""
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount
    api_key = os.getenv("API_KEY") or ""
    response = requests.get(
        "https://api.apilayer.com/exchangerates_data/convert",
        params={
            "to": "RUB",
            "from": currency,
            "amount": amount,
        },
        headers={"apikey": api_key},
    )
    return float(response.json()["result"])
