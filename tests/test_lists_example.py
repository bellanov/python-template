import importlib
import sys


def test_lists_example():
    """
    Test list operations defined in lists_example.py
    """

    # Import a fresh copy of the module
    if "lists_example" in sys.modules:
        del sys.modules["lists_example"]
    lists_example = importlib.import_module("lists_example")

    # ---- Check initial and modified list values ----
    my_list = lists_example.my_list

    # After modifications and operations in the script
    # Expected list:
    # Start: [1, 2, 3, 'four', 'five', 6.0]
    # Step 1: my_list[1] = 'two' -> [1, 'two', 3, 'four', 'five', 6.0]
    # Step 2: append(7) -> [1, 'two', 3, 'four', 'five', 6.0, 7]
    # Step 3: insert(0, 0) -> [0, 1, 'two', 3, 'four', 'five', 6.0, 7]
    # Step 4: remove('four') -> [0, 1, 'two', 3, 'five', 6.0, 7]
    # Step 5: pop() -> last element 7 removed -> [0, 1, 'two', 3, 'five', 6.0]

    expected_list = [0, 1, "two", 3, "five", 6.0]
    assert my_list == expected_list

    # ---- Access elements ----
    assert lists_example.first_element == 1
    assert lists_example.last_element == 6.0

    # ---- Slicing ----
    expected_sublist = [1, "two", 3]
    assert lists_example.sub_list == expected_sublist

    # ---- Length ----
    assert lists_example.list_length == len(my_list)

    # ---- Popped element ----
    assert lists_example.popped_element == 7


def test_lists_example_print(capsys):
    # Test the print output of lists_example.py module

    captured = capsys.readouterr()
    output = captured.out

    # Check that some known values are printed
    assert "Length of the list:" in output
    assert "0" in output  # First element after insertion
