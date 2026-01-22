"""
A tuple is an ordered, immutable collection of elements.
Once a tuple is created, its elements cannot be modified, added, or removed.
Tuples are commonly used to group related data together and can contain elements of different types.

"""

# Creating a tuple
tuple1 = (1, 2, "three", 4.0)
tuple2 = (5, 6, 7)

# Accessing elements in a tuple
print(tuple1[0])  # Output: 1
print(tuple1[2])  # Output: "three"
print(tuple2[-1])  # Output: 7

# Tuple concatenation
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, "three", 4.0, 5, 6, 7)
