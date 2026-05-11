"""Test the Hello World sample."""

import pytest

from samples.dsa.retry_pattern import retry


@pytest.mark.unit  # type: ignore
def test_retry():
    """Test the retry function."""
    assert retry.retry() == True
