"""
Function module - Demonstrates the definition and usage of functions in Python.
functions are reusable blocks of code that perform a specific task.
They help in organizing code, improving readability, and reducing redundancy.
Functions can take inputs (parameters) and can return outputs (return values).

"""


# Defining a function
def greet(name):
    """This function greets the person passed in as a parameter."""
    return f"Hello, {name}!"


# Calling the function
message = greet("Alice")
print(message)  # Output: Hello, Alice!


# Function with multiple parameters
def add_numbers(a, b):
    """This function returns the sum of two numbers."""
    return a + b


sum_result = add_numbers(5, 7)
print(sum_result)  # Output: 12


# Function with default parameter
def power(base, exponent=2):
    """This function returns the base raised to the power of exponent."""
    return base**exponent


squared = power(4)
cubed = power(3, 3)
print(squared)  # Output: 16
print(cubed)  # Output: 27


# Function with variable number of arguments
def multiply(*args):
    """This function returns the product of all the numbers passed as arguments."""
    product = 1
    for num in args:
        product *= num
    return product


result = multiply(2, 3, 4)
print(result)  # Output: 24


# Function with keyword arguments
def introduce(**kwargs):
    """This function introduces a person using keyword arguments."""
    introduction = ", ".join(f"{key}: {value}" for key, value in kwargs.items())
    return f"Introduction: {introduction}"


intro_message = introduce(name="Bob", age=30, city="New York")
print(intro_message)  # Output: Introduction: name: Bob, age: 30
