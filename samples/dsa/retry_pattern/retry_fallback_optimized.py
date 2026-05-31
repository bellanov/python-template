"""Retry Pattern.

The retry pattern is a design pattern that allows you to automatically retry a failed operation a
certain number of times before giving up. This can be useful for handling transient errors, such as
network issues or temporary unavailability of a service.
"""

import random
import time
from typing import Callable

import httpx


def retry[T](
    operations: list[Callable[..., T]],
    delay: float = 1.0,
    backoff: float = 2.0,
) -> T:

    if not operations:
        raise ValueError("At least one operation must be provided.")

    for attempt, operation in enumerate(operations):
        try:
            return operation()
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            sleep_time = delay * (backoff ** (attempt - 1))
            print(f"Retrying in {sleep_time:.2f} seconds...")
            time.sleep(sleep_time)

    raise RuntimeError("All retry attempts failed.")


def fetch_backup_api() -> str:
    """Fetch a random joke from a backup API."""
    return "Backup joke: Why don't scientists trust atoms? Because they make up everything!"


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
    print(retry([fetch_joke] * 3 + [fetch_backup_api]))


if __name__ == "__main__":
    main()
