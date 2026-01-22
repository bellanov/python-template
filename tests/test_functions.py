import pytest
from functions import add_numbers, greet, introduce, multiply, power


def test_greet():
    """Test greeting function."""
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"


def test_add_numbers():
    """Test adding two numbers."""
    assert add_numbers(5, 7) == 12
    assert add_numbers(-1, 1) == 0
    assert add_numbers(2, 3) == 5


def test_power_default_exponent():
    """Test power function with default exponent."""
    assert power(4) == 16


def test_power_custom_exponent():
    """Test power function with custom exponent."""
    assert power(3, 3) == 27
    assert power(2, 4) == 16


def test_multiply_multiple_args():
    """Test multiplying multiple values."""
    assert multiply(2, 3, 4) == 24
    assert multiply(1, 2, 3, 4) == 24


def test_multiply_single_arg():
    """Test multiplying a single value."""
    assert multiply(5) == 5


def test_multiply_no_args():
    """Test multiplying with no arguments (identity value)."""
    assert multiply() == 1


def test_introduce():
    """Test keyword argument introduction."""
    result = introduce(name="Bob", age=30, city="New York")
    assert "name: Bob" in result
    assert "age: 30" in result
    assert "city: New York" in result
    assert result.startswith("Introduction:")
