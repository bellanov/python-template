"""Examples of validating and serializing data with Pydantic."""

from pydantic import BaseModel, ConfigDict, Field


class Address(BaseModel):
    """A nested model with validated fields."""

    model_config = ConfigDict(extra="forbid")

    street: str = Field(min_length=1)
    city: str = Field(min_length=1)
    postal_code: str = Field(min_length=1)


class User(BaseModel):
    """A user model with constraints, nested data, and a safe mutable default."""

    model_config = ConfigDict(extra="forbid")

    id: int = Field(gt=0)
    name: str = Field(min_length=1)
    address: Address
    tags: list[str] = Field(default_factory=list)


def main() -> None:
    """Validate JSON input and print the normalized JSON representation."""
    payload = """
    {
        "id": 1,
        "name": "Ada Lovelace",
        "address": {
            "street": "12 Analytical Engine Way",
            "city": "London",
            "postal_code": "N1 1AA"
        },
        "tags": ["admin", "researcher"]
    }
    """
    user = User.model_validate_json(payload)
    print(user.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
