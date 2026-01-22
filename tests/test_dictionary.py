import importlib
import sys
from typing import Any

from pytest import CaptureFixture


def test_dictionary_example_values():
    """
    Test dictionary creation, updates, deletions,
    and methods in dictionary_example.py
    """

    # Import a fresh copy of the module
    if "dictionary_example" in sys.modules:
        del sys.modules["dictionary_example"]
    dictionary_example = importlib.import_module("dictionary_example")

    # ---- Initial values ----
    assert dictionary_example.name == "Alice"
    assert dictionary_example.age == 31  # Updated age
    assert "is_student" not in dictionary_example.my_dict
    assert dictionary_example.city == "New York"

    # ---- Keys, values, items ----
    keys = list(dictionary_example.keys)
    values = list(dictionary_example.values)
    items: list[Any] = list(dictionary_example.items)

    assert "name" in keys
    assert "age" in keys
    assert "city" in keys

    assert "Alice" in values
    assert 31 in values
    assert "New York" in values

    # ---- Length check ----
    assert dictionary_example.dict_length == 3

    # ---- Key existence ----
    assert dictionary_example.has_name is True


def test_dictionary_example_print(capsys: CaptureFixture[str]):
    # Test the print output of dictionary_example.py

    captured = capsys.readouterr()
    output = captured.out

    assert "name: Alice" in output
    assert "age: 31" in output
    assert "city: New York" in output
