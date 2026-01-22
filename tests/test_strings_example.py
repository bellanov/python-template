import importlib
import sys


def test_strings_example():
    """
    Test string operations defined in strings_example.py
    """

    # Import a fresh copy of the module
    if "strings_example" in sys.modules:
        del sys.modules["strings_example"]
    strings_example = importlib.import_module("strings_example")

    # ---- String creation ----
    assert strings_example.string1 == "Hello, World!"
    assert strings_example.string2 == "Python Programming"

    # ---- Character access ----
    assert strings_example.first_char == "H"
    assert strings_example.last_char == "g"

    # ---- Concatenation ----
    expected_greeting = "Hello, World! Python Programming"
    assert strings_example.greeting == expected_greeting

    # ---- Repetition ----
    expected_repeat = "Hello, World!" * 3
    assert strings_example.repeat_hello == expected_repeat

    # ---- Slicing ----
    assert strings_example.sub_string == "Python"

    # ---- String methods ----
    assert strings_example.upper_string == "HELLO, WORLD!"
    assert strings_example.lower_string == "python programming"
    assert strings_example.replace_string == "Hello, Python!"

    # ---- Split ----
    assert strings_example.words == ["Python", "Programming"]


def test_strings_example_print(capsys):

    captured = capsys.readouterr()
    output = captured.out

    assert "Hello, World! Python Programming" in output
    assert "Hello, World!Hello, World!Hello, World!" in output
    assert "Python" in output
    assert "HELLO, WORLD!" in output
    assert "python programming" in output
    assert "Hello, Python!" in output
    assert "['Python', 'Programming']" in output
