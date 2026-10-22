# Pydantic

Overview of *Pydantic* and it's usage.

Pydantic is a data validation and settings management library for Python, based on Python type annotations. It allows you to define data models with type hints, and automatically validates and parses input data according to those types.

The `CamelCaseModel` is a base model that uses `camelCase` aliasing for its attributes, instead of `snake_case`. This means that when the model is serialized to JSON or other formats, the attribute names will be converted to camelCase format. It also supports ORM integration, allowing for easy conversion from ORM objects to Pydantic models.

Setting the `alias_generator` value to `to_camel` allows the model to automatically convert attribute names from `snake_case` to `camelCase` when serializing to **JSON** or other formats. The `populate_by_name` option allows the model to accept input data in either `snake_case` or `camelCase` format, making it more flexible for different use cases. The `from_attributes` option allows the model to be populated from ORM objects, making it easier to work with databases and other data sources.

```python
class CamelCaseModel(BaseModel):
    """Base model with camelCase aliasing and ORM integration.

    This model exports attributes in camelCase format, making it suitable
    for APIs that expect camelCase keys. It also supports ORM integration,
    allowing for easy conversion from ORM objects to Pydantic models.

    Attributes:
        model_config: Configuration for the Pydantic model.
    """

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,  # Allows python to parse snake_case if needed
        from_attributes=True,  # Helps with ORM integration like SQLAlchemy
    )
```