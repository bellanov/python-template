import importlib
import sys


def test_sets_example():
    """
    Test set operations defined in sets_example.py
    """

    # Import a fresh copy of the module
    if "sets_example" in sys.modules:
        del sys.modules["sets_example"]
    sets_example = importlib.import_module("sets_example")

    # ---- Original set after additions/removals ----
    # Start: {1, 2, "three", 4.0}
    # Step 1: add(5) -> {1, 2, "three", 4.0, 5}
    # Step 2: remove("three") -> {1, 2, 4.0, 5}
    expected_set = {1, 2, 4.0, 5}
    assert sets_example.my_set == expected_set

    # ---- Membership test ----
    assert sets_example.is_member is True

    # ---- Another set ----
    assert sets_example.another_set == {4.0, 5, 6, 7}

    # ---- Union ----
    expected_union = {1, 2, 4.0, 5, 6, 7}
    assert sets_example.union_set == expected_union


def test_sets_example_print(capsys):  # Test the print output of sets_example.py module

    captured = capsys.readouterr()
    output = captured.out 

    # Example checks (if you added prints)
    # assert "1" in output
    # assert "5" in output
