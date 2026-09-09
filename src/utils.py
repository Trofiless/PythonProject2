import json
import logging
from pathlib import Path

LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(LOGS_DIR / "utils.log", mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def load_operations(file_path: str) -> list[dict]:
    """Загружает финансовые операции из JSON-файла."""
    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        logger.error("Ошибка загрузки файла %s: %s", file_path, error)
        return []
    if not isinstance(data, list):
        logger.error("Данные в файле %s не являются списком", file_path)
        return []
    logger.info("Файл %s успешно загружен", file_path)
    return data
