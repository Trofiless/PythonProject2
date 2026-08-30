from typing import Any, Iterable, Iterator


def filter_by_currency(transactions: Iterable[dict[str, Any]], currency: str) -> Iterator[dict[str, Any]]:
    """Возвращает генератор транзакций по указанной валюте."""

    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(
    transactions: Iterable[dict[str, Any]],
) -> Iterator[str]:
    """Возвращает описания транзакций по одной."""

    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX."""

    for number in range(start, stop + 1):
        card_number = f"{number:016d}"
        yield (f"{card_number[:4]} " f"{card_number[4:8]} " f"{card_number[8:12]} " f"{card_number[12:]}")
