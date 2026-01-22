"""
Docstring for samples.len_examples
This module demonstrates the use of the len() function
to determine the length of various data structures in Python.

"""

# String
length_str: int = len("hello world")
print(length_str)  # 11


# List
numbers: list[int] = [10, 20, 30, 40]
length_list: int = len(numbers)
print(length_list)  # 4


# Tuple
coords: tuple[int, int, int] = (1, 2, 3)
length_tuple: int = len(coords)
print(length_tuple)  # 3


# Dictionary
mapping: dict[str, int] = {"a": 1, "b": 2}
length_dict: int = len(mapping)
print(length_dict)  # 2


# Set
unique_values: set[int] = {1, 2, 3, 4, 5}
length_set: int = len(unique_values)
print(length_set)  # 5
