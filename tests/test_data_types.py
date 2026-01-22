import importlib
import sys

from pytest import CaptureFixture


def test_data_types_module_values():
    """
    Test integer, float, string, and boolean examples
    defined in data_types.py.
    """

    # Import fresh copy of the module (important because it runs on import)
    if "data_types" in sys.modules:
        del sys.modules["data_types"]

    data_types = importlib.import_module("data_types")

    # ---- Integer tests ----
    assert data_types.result1 == 10
    assert isinstance(data_types.result1, int)

    assert data_types.result2 == 5
    assert isinstance(data_types.result2, int)

    # ---- Float tests ----
    assert data_types.result3 == 10.2
    assert isinstance(data_types.result3, float)

    assert data_types.result4 == 2.5
    assert isinstance(data_types.result4, float)

    # ---- String test ----
    assert data_types.c == "Hello, Python!"
    assert isinstance(data_types.c, str)

    # ---- Boolean tests ----
    assert data_types.d is True
    assert isinstance(data_types.d, bool)

    assert data_types.e is False
    assert isinstance(data_types.e, bool)

    # ---- Boolean arithmetic behavior ----
    assert (True + True) == 2
    assert (False + True) == 1
    assert (False + False) == 0


def test_data_types_print_output(capsys: CaptureFixture[str]):
    # Test the print output of data_types.py module
    captured = capsys.readouterr()

    assert "Integer:" in captured.out
    assert "Float:" in captured.out
    assert "String:" in captured.out
    assert "Boolean:" in captured.out
