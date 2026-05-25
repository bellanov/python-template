"""Retry Pattern.

The retry pattern is a design pattern that allows you to automatically retry a failed operation a
certain number of times before giving up. This can be useful for handling transient errors, such as
network issues or temporary unavailability of a service.
"""

import random
import time
from functools import wraps
from typing import Any, Callable

import httpx


def retry_decorator[T](
    backup_fn: Callable[..., T],
    retries: int = 5,
    delay: float = 1.0,
    backoff: float = 2.0,
) -> Callable[..., T]:
    """Define a decorator for retrying a function upon failure.

    Args:
        backup_fn: A callable that provides a fallback result if all retry attempts fail.
        retries: The maximum number of retry attempts.
        delay: The delay in seconds between retry attempts.
        backoff: The multiplier for the delay between attempts (exponential backoff).

    Returns:
        The decorated function.
    """

    def decorator[T](operation: Callable[..., T]) -> Callable[..., T]:
        """Retry the given operation a certain number of times with a delay between attempts.

        Args:
            operation: A callable that performs the operation to be retried.

        Returns:
            The result of the operation if it succeeds. If all retry attempts fail, the result
            of the backup function is returned.
        """

        @wraps(operation)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            """Wrap the operation with retry logic."""
            for attempt in range(1, retries + 1):
                try:
                    return operation()
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt == retries:
                        print("All retry attempts failed. Using backup function...")
                        return backup_fn()
                    sleep_time = delay * (backoff ** (attempt - 1))
                    print(f"Retrying in {sleep_time:.2f} seconds...")
                    time.sleep(sleep_time)

            return backup_fn()

        return wrapper

    return decorator


def fetch_backup_api() -> str:
    """Fetch a random joke from a backup API."""
    return "Backup joke: Why don't scientists trust atoms? Because they make up everything!"


@retry_decorator(backup_fn=fetch_backup_api)
def fetch_joke() -> str:
    """Fetch a random Chuck Norris joke from the API."""
    # Randomly raise an exception to simulate a transient error
    if random.random() < 0.6:
        raise httpx.HTTPError("Simulated transient error")
    with httpx.Client() as client:
        response = client.get("https://api.chucknorris.io/jokes/random")
        response.raise_for_status()
        data: dict[str, str] = response.json()
        return data["value"]


def main() -> None:
    print(fetch_joke())


if __name__ == "__main__":
    main()
