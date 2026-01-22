import importlib
import sys


def test_tuples_example():
    """
    Test tuple operations defined in tuples_example.py
    """

    # Import a fresh copy of the module
    if "tuples_example" in sys.modules:
        del sys.modules["tuples_example"]
    tuples_example = importlib.import_module("tuples_example")

    # ---- Tuple creation ----
    assert tuples_example.tuple1 == (1, 2, "three", 4.0)
    assert tuples_example.tuple2 == (5, 6, 7)

    # ---- Element access ----
    assert tuples_example.tuple1[0] == 1
    assert tuples_example.tuple1[2] == "three"
    assert tuples_example.tuple2[-1] == 7

    # ---- Concatenation ----
    expected_combined = (1, 2, "three", 4.0, 5, 6, 7)
    assert tuples_example.combined_tuple == expected_combined


def test_tuples_example_print(capsys):

    captured = capsys.readouterr()
    output = captured.out

    assert "1" in output
    assert "three" in output
    assert "7" in output
    assert "(1, 2, 'three', 4.0, 5, 6, 7)" in output
