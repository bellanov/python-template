"""Unit tests for the Pydantic sample."""

import pytest
from pydantic import ValidationError

from samples.pydantic.pydantic import User


@pytest.mark.unit
def test_user_validates_nested_data_and_uses_empty_tags_by_default():
    user = User.model_validate(
        {
            "id": 1,
            "name": "Ada Lovelace",
            "address": {
                "street": "12 Analytical Engine Way",
                "city": "London",
                "postal_code": "N1 1AA",
            },
        }
    )

    assert user.address.city == "London"
    assert user.tags == []


@pytest.mark.unit
@pytest.mark.parametrize(
    "payload",
    [
        {
            "id": 0,
            "name": "Ada",
            "address": {
                "street": "1 Main Street",
                "city": "London",
                "postal_code": "N1 1AA",
            },
        },
        {
            "id": 1,
            "name": "Ada",
            "address": {
                "street": "1 Main Street",
                "city": "London",
                "postal_code": "N1 1AA",
                "country": "UK",
            },
        },
    ],
)
def test_user_rejects_invalid_values_and_unexpected_fields(payload):
    with pytest.raises(ValidationError):
        User.model_validate(payload)


@pytest.mark.unit
def test_user_serializes_to_json():
    user = User(
        id=1,
        name="Ada Lovelace",
        address={
            "street": "12 Analytical Engine Way",
            "city": "London",
            "postal_code": "N1 1AA",
        },
        tags=["researcher"],
    )

    assert '"name":"Ada Lovelace"' in user.model_dump_json()
