"""Retry Pattern.

The retry pattern is a design pattern that allows you to automatically retry a failed operation a 
certain number of times before giving up. This can be useful for handling transient errors, such as 
network issues or temporary unavailability of a service.
"""

import random
import httpx
import time
from typing import Callable

def retry[T](operation: Callable[[], T], retries: int = 5, delay: float = 1.0, backoff: float = 2.0) -> T:
    """Retry the given operation a certain number of times with a delay between attempts.
    
    Args:
        operation: A callable that performs the operation to be retried.
        retries: The maximum number of retry attempts.
        delay: The delay in seconds between retry attempts.

    Returns:
        The result of the operation if it succeeds.

    Raises:
        The last exception raised by the operation if all retry attempts fail.
    
    """
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


def fetch_joke() -> str:
    """Fetch a random Chuck Norris joke from the API."""
    # Randomly raise an exception to simulate a transient error
    if random.random() < 0.7:
        raise httpx.HTTPError("Simulated transient error")
    with httpx.Client() as client:
        response = client.get("https://api.chucknorris.io/jokes/random")
        response.raise_for_status()
        data: dict[str, str] = response.json()
        return data["value"]


def main() -> None:
    joke = retry(fetch_joke)
    print(joke)


if __name__ == "__main__":
    main()