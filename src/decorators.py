import logging
from functools import wraps
from typing import Any


def log(filename: str | None = None) -> Any:
    """Логирует успешное выполнение функции и возникающие ошибки."""

    def decorator(func: Any) -> Any:
        """Создает обертку для логирования функции."""

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Логирует выполнение функции и возникающие ошибки."""
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)
            handler: logging.Handler
            if filename:
                handler = logging.FileHandler(filename)
            else:
                handler = logging.StreamHandler()
            logger.addHandler(handler)
            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as error:
                logger.error(f"{func.__name__} error: {type(error).__name__}. " f"Inputs: {args}, {kwargs}")
                raise
            finally:
                logger.removeHandler(handler)
                handler.close()

        return wrapper

    return decorator
