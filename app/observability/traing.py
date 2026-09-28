import time
from functools import wraps


def trace(name: str):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            start_time = time.time()

            print("\n" + "-" * 60)
            print(f"TRACE START: {name}")
            print("-" * 60)

            try:
                result = func(*args, **kwargs)

                return result

            except Exception as error:

                print(f"ERROR: {error}")

                raise

            finally:

                end_time = time.time()
                duration = end_time - start_time

                print("-" * 60)
                print(f"TRACE END: {name}")
                print(f"Duration: {duration:.2f} seconds")
                print("-" * 60)

        return wrapper

    return decorator