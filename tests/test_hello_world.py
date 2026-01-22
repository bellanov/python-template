import importlib
import sys


def test_hello_world():
    """
    Test that hello_world() returns the correct string.
    """

    # Import a fresh copy of the module
    if "hello" in sys.modules:
        del sys.modules["hello"]
    hello = importlib.import_module("hello")

    # Call the function and check output
    result = hello.hello_world()
    assert result == "Hello, World!"
