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