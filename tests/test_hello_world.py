"""Test the Hello World sample."""
import pytest

from samples.hello_world.app import hello_world


@pytest.mark.unit  # type: ignore
def test_hello_world():
    """Test the hello_world function."""
    assert hello_world() == "Hello, World!"
