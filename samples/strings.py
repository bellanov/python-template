""" "
Define strings and demonstrate basic operations
Strings are sequences of characters enclosed in single or double quotes
They are immutable, meaning they cannot be changed after creation

"""

import sys

# Creating strings
string1 = "Hello, World!"
string2 = "Python Programming"

# Accessing characters in a string
first_char = string1[0]  # Accessing the first character
last_char = string2[-1]  # Accessing the last character

# String concatenation
greeting = string1 + " " + string2
print(greeting)  # Output: Hello, World! Python Programming

# String repetition
repeat_hello = string1 * 3
print(repeat_hello)  # Output: Hello, World!Hello, World!Hello

# String slicing
sub_string = string2[0:6]  # Getting a substring from index 0
print(sub_string)  # Output: Python

# String methods
upper_string = string1.upper()  # Convert to uppercase
print(upper_string)  # Output: HELLO, WORLD!

lower_string = string2.lower()  # Convert to lowercase
print(lower_string)  # Output: python programming

replace_string = string1.replace("World", "Python")  # Replace substring
print(replace_string)  # Output: Hello, Python!

# Splitting a string
words = string2.split(" ")  # Split string into a list of words
print(words)  # Output: ['Python', 'Programming']

# LAB: Coding with Python Strings


sys.version_info[0]

lab_exercise = "Count"
lab_type = "lab-code"
python_version = "%s.%s.%s" % (
    sys.version_info[0],
    sys.version_info[1],
    sys.version_info[2],
)
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

# ====================================

data = "cloudacademy.python.2019"
letter1 = "a"
word1 = "cloud"
num1 = "2019"

# CODE1: Count occurrences of letters and words
print(f"Count '{letter1}' = {data.count(letter1)}")
print(f"count '{word1}' = {data.count(word1)}")
print(f"count '{num1}' = {data.count(num1)}")
print()

# CODE2: Get length of string
print(len(data))
print()

# CODE3: Get max of string - the highest char in the string
print(f" Max of string: {max(data)}")
print()

# CODE4: Get min of string - the lowest char in the string
print(f" Min of string: {min(data)}")
print()
