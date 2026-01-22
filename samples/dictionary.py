"""
Dictionary is a built-in data type in Python that stores key-value pairs.
Each key is unique and is used to access its corresponding value.
Dictionaries are mutable, meaning you can add, remove, or modify items.
They are commonly used for storing and retrieving data efficiently.

"""

# Creating a dictionary
my_dict = {"name": "Alice", "age": 30, "is_student": False}

# Accessing values
name = my_dict["name"]
age = my_dict.get("age", 0)  # Default to 0 if key not found

# Adding or updating key-value pairs
my_dict["age"] = 31
my_dict["city"] = "New York"

# Removing key-value pairs
del my_dict["is_student"]

# Dictionary methods
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

# Iterating through a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Checking if a key exists
has_name = "name" in my_dict  # Returns True

# Getting the length of a dictionary
dict_length = len(my_dict)
