"""Test the PYTHONPATH sample."""
import pytest

from samples.beginner.pythonpath.app import display_pythonpath


def test_display_pythonpath():
    """Test the display_pythonpath function."""
    assert display_pythonpath() is None
