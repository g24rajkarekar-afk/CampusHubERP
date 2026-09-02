import time
from functools import wraps


def log_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):

        print(f"\nFunction Started: {function.__name__}")

        result = function(*args, **kwargs)

        print(f"Function Completed: {function.__name__}")

        return result

    return wrapper


def time_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):

        start_time = time.time()

        result = function(*args, **kwargs)

        end_time = time.time()

        execution_time = end_time - start_time

        print(
            f"Execution Time ({function.__name__}): "
            f"{execution_time:.6f} seconds"
        )

        return result

    return wrapper