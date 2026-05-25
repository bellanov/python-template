"""Retry Pattern.

The retry pattern is a design pattern that allows you to automatically retry a failed operation a 
certain number of times before giving up. This can be useful for handling transient errors, such as 
network issues or temporary unavailability of a service.
"""

import random
import httpx
import time
from typing import Callable, Any
from functools import wraps


def retry_decorator[T](retries: int = 5, delay: float = 1.0, backoff: float = 2.0) -> Callable[..., T]:
    """Define a decorator for retrying a function upon failure.
        
        Args:
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
            The result of the operation if it succeeds.

        Raises:
            The last exception raised by the operation if all retry attempts fail.
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
                        raise
                    sleep_time = delay * (backoff ** (attempt - 1))
                    print(f"Retrying in {sleep_time:.2f} seconds...")
                    time.sleep(sleep_time)

        return wrapper
    return decorator

@retry_decorator()
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