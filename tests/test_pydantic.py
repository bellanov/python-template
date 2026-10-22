"""Unit tests for the Pydantic sample."""

import pytest
from pydantic import Field

from samples.pydantic.camel_case import CamelCaseModel


class Folder(CamelCaseModel):
    """Represents a folder.

    Attributes:
        id: The ID of the folder.
        name: The name of the folder.
    """

    name: str = Field()
    parent: str = Field()
    display_name: str = Field()


@pytest.mark.unit
def test_camel_case_model():
    folder = Folder(name="folders/123", parent="folders/456", display_name="My Folder")
    assert folder.name == "folders/123"
    assert folder.parent == "folders/456"
    assert folder.display_name == "My Folder"
