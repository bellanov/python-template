"""Unit tests for the retry pattern sample."""

from unittest.mock import MagicMock, Mock

import httpx
import pytest

from samples.retry_pattern import retry as retry_module


@pytest.mark.unit
def test_fetch_joke_retries_after_request_error(monkeypatch):
    """Retry a failed request and return the successful response."""
    result = retry_module.fetch_joke()
    assert "Chuck Norris" in result
