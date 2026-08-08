def filter_by_currency(transactions, currency):
    """Возвращает генератор транзакций по указанной валюте."""

    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions):
    """Возвращает описания транзакций по одной."""

    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, stop):
    """Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX."""

    for number in range(start, stop + 1):
        card_number = f"{number:016d}"
        yield (f"{card_number[:4]} " f"{card_number[4:8]} " f"{card_number[8:12]} " f"{card_number[12:]}")
