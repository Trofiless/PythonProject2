import pytest

from src.processing import filter_by_state, sort_by_date


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