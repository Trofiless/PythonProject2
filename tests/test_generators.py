import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(operations):
    usd_transactions = list(filter_by_currency(operations, "USD"))

    assert len(usd_transactions) == 3
    assert usd_transactions[0]["operationAmount"]["currency"]["code"] == "USD"
    assert usd_transactions[1]["operationAmount"]["currency"]["code"] == "USD"
    assert usd_transactions[2]["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_not_found(operations):
    result = list(filter_by_currency(operations, "EUR"))

    assert result == []


def test_transaction_descriptions(operations):
    descriptions = list(transaction_descriptions(operations))

    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1,
            3,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
            ],
        ),
        (
            5,
            5,
            [
                "0000 0000 0000 0005",
            ],
        ),
    ],
)
def test_card_number_generator(start, stop, expected):
    cards = list(card_number_generator(start, stop))
    assert cards == expected


def test_card_number_generator_format():
    card = next(card_number_generator(1, 1))

    assert len(card) == 19
    assert card == "0000 0000 0000 0001"
