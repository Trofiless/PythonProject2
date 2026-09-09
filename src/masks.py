import logging
from pathlib import Path

LOGS_DIR = Path("logs")

LOGS_DIR.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

handler = logging.FileHandler(LOGS_DIR / "masks.log", mode="w", encoding="utf-8")

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

handler.setFormatter(formatter)

logger.addHandler(handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскировка номера карты."""

    if len(card_number) != 16:

        logger.error("Некорректный номер карты")

        raise ValueError("Номер карты должен содержать 16 цифр")

    logger.info("Номер карты успешно замаскирован")

    return f"{card_number[:4]} " f"{card_number[4:6]}** " f"**** " f"{card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскировка номера счета."""

    if len(account_number) < 20:

        logger.error("Некорректный номер счета")

        raise ValueError("Номер счета должен содержать минимум 20 цифр")

    logger.info("Номер счета успешно замаскирован")

    return f"**{account_number[-4:]}"
