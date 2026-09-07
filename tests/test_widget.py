import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "data, expected",
    [
        ("Visa Platinum 1234567812345678", "Visa Platinum 1234 56** **** 5678"),
        ("Maestro 1111222233334444", "Maestro 1111 22** **** 4444"),
        ("Счет 12345678901234567890", "Счет **7890"),
    ],
)
def test_mask_account_card(data: str, expected: str):
    assert mask_account_card(data) == expected


def test_mask_account_card_invalid():
    with pytest.raises(ValueError):
        mask_account_card("1234567890")


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-01-01T00:00:00", "01.01.2023"),
    ],
)
def test_get_date(date_string: str, expected: str):
    assert get_date(date_string) == expected


def test_get_date_invalid():
    with pytest.raises(ValueError):
        get_date("не дата")
