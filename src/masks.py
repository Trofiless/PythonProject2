def get_mask_card_number(card_number: str) -> str:
    """Маскировка номера карты."""

    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    return f"{card_number[:4]} " f"{card_number[4:6]}** " f"**** " f"{card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскировка номера счета."""

    if len(account_number) != 20:
        raise ValueError("Номер счета должен содержать минимум 20 цифр")

    return f"**{account_number[-4:]}"
