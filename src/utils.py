import json


def load_operations(file_path: str) -> list[dict]:
    """Загружает финансовые операции из JSON-файла."""

    try:

        with open(file_path, encoding="utf-8") as file:

            data = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):

        return []

    if not isinstance(data, list):

        return []

    return data
