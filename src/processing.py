import re
from collections import Counter


def filter_by_state(
    operations: list[dict],
    state: str = "EXECUTED",
) -> list[dict]:
    """Фильтрация операций по статусу."""

    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(
    operations: list[dict],
    reverse: bool = True,
) -> list[dict]:
    """Сортировка операций по дате."""

    return sorted(
        operations,
        key=lambda operation: operation["date"],
        reverse=reverse,
    )


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Ищет операции по строке в поле description."""

    pattern = re.compile(search, re.IGNORECASE)

    return [operation for operation in data if pattern.search(operation.get("description", ""))]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Подсчитывает количество операций по категориям."""

    result = Counter()

    for operation in data:

        description = operation.get("description", "").lower()

        for category in categories:

            if category.lower() in description:

                result[category] += 1

    return dict(result)
