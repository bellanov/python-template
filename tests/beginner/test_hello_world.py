"""Test the Hello World sample."""
import pytest

from samples.beginner.hello_world.app import hello_world


def test_hello_world():
    """Test the hello_world function."""
    assert hello_world() == "Hello, World!"
