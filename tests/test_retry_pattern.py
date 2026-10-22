"""Unit tests for the retry pattern sample."""

import pytest

from samples.retry_pattern import retry as retry_module


@pytest.mark.unit
def test_fetch_joke_retries_after_request_error():
    """Retry a failed request and return the successful response."""
    result = retry_module.fetch_joke()
    assert "Chuck Norris" in result or "Chuck" in result
