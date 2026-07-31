import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1111222233334444", "1111 22** **** 4444"),
    ],
)
def test_get_mask_card_number(card, expected):
    assert get_mask_card_number(card) == expected


def test_get_mask_card_number_invalid():
    with pytest.raises(ValueError):
        get_mask_card_number("123")


@pytest.mark.parametrize(
    "account, expected",
    [
        ("12345678901234567890", "**7890"),
        ("11111111111111111111", "**1111"),
    ],
)
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected


def test_get_mask_account_invalid():
    with pytest.raises(ValueError):
        get_mask_account("123")
