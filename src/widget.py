from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(data: str) -> str:
    parts = data.split()

    if len(parts) < 2:
        raise ValueError("Некорректный ввод")

    number = parts[-1]
    name = " ".join(parts[:-1])

    if name == "Счет":
        return f"{name} {get_mask_account(number)}"

    return f"{name} {get_mask_card_number(number)}"

def get_date(date_string: str) -> str:
    date_obj = datetime.fromisoformat(date_string)

    return date_obj.strftime("%d.%m.%Y")