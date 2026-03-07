# content of test_approx.py
import pytest

from samples.beginner.hello_world.hello_world import hello_world


def test_hello_world():
    assert hello_world() == "Hello, World!"
