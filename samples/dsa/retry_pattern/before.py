"""Retry Pattern.

The retry pattern is a design pattern that allows you to automatically retry a failed operation a
certain number of times before giving up. This can be useful for handling transient errors, such as
network issues or temporary unavailability of a service.
"""

import random

import httpx


def fetch_joke() -> str:
    """Fetch a random Chuck Norris joke from the API."""
    # Randomly raise an exception to simulate a transient error
    if random.random() < 0.5:
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
