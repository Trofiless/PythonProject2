from functools import wraps
import logging

def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)
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
                logger.error(
                    f"{func.__name__} error: {type(error).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )
                raise
            finally:
                logger.removeHandler(handler)
                handler.close()
        return wrapper
    return decorator

