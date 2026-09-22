from src.processing import (
    filter_by_state,
    process_bank_operations,
    process_bank_search,
    sort_by_date,
)

operations = [
    {
        "id": 1,
        "state": "EXECUTED",
        "date": "2024-03-11T02:26:18.671407",
    },
    {
        "id": 2,
        "state": "CANCELED",
        "date": "2023-01-01T00:00:00",
    },
    {
        "id": 3,
        "state": "EXECUTED",
        "date": "2025-05-10T10:00:00",
    },
]


def test_filter_by_state_default():
    result = filter_by_state(operations)

    assert len(result) == 2
    assert all(operation["state"] == "EXECUTED" for operation in result)


def test_filter_by_state_custom():
    result = filter_by_state(operations, "CANCELED")

    assert len(result) == 1
    assert result[0]["state"] == "CANCELED"


def test_filter_by_state_empty():
    result = filter_by_state(operations, "PENDING")

    assert result == []


def test_sort_by_date_desc():
    result = sort_by_date(operations)

    assert result[0]["date"] == "2025-05-10T10:00:00"
    assert result[-1]["date"] == "2023-01-01T00:00:00"


def test_sort_by_date_asc():
    result = sort_by_date(operations, reverse=False)

    assert result[0]["date"] == "2023-01-01T00:00:00"
    assert result[-1]["date"] == "2025-05-10T10:00:00"


search_operations = [
    {
        "id": 1,
        "description": "Перевод с карты на карту",
    },
    {
        "id": 2,
        "description": "Оплата продуктов",
    },
    {
        "id": 3,
        "description": "Перевод организации",
    },
]


def test_process_bank_search_found():

    result = process_bank_search(search_operations, "перевод")

    assert len(result) == 2

    assert result[0]["id"] == 1

    assert result[1]["id"] == 3


def test_process_bank_search_case_insensitive():

    result = process_bank_search(search_operations, "ПЕРЕВОД")

    assert len(result) == 2


def test_process_bank_search_not_found():

    result = process_bank_search(search_operations, "зарплата")

    assert result == []


def test_process_bank_operations():

    categories = ["Перевод", "Оплата"]

    result = process_bank_operations(search_operations, categories)

    assert result == {
        "Перевод": 2,
        "Оплата": 1,
    }
