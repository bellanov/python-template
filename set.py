"""
This module demonstrates the use of sets in Python.
A set is an unordered collection of unique elements. Sets are mutable, meaning you can add or remove elements after creation. They are commonly used for membership testing, eliminating duplicate entries, and performing mathematical set operations like union, intersection, and difference.

"""

my_set = {1, 2, "three", 4.0}
# Accessing elements in a set (Note: sets are unordered)

# Checking membership
is_member = 2 in my_set  # Returns True

# Adding elements to a set
my_set.add(5)

# Removing elements from a set
my_set.remove("three")  # Raises KeyError if element not found
my_set.discard(10)  # Does not raise an error if element not found

# Set operations
another_set = {4.0, 5, 6, 7}

# Union
union_set = my_set.union(another_set)
