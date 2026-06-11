def filter_by_state(
    operations: list[dict],
    state: str = "EXECUTED",
) -> list[dict]:
    """Фильтрация операций по статусу."""

    return [
        operation
        for operation in operations
        if operation.get("state") == state
    ]

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