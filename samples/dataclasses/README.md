# Dataclasses

Overview of *Dataclasses* and their usage.

# Background

Some programming languages provide a more **data-oriented** version of a `Class`. For instance, **C#** has the `Struct` type that is more suited to represent data structures.

In *Python 3.7*, the **Dataclasses** module was made available.

How are *Dataclasses* different than regular *Classes*?

- They have a built-in initializer that helps you fill in objects very quickly.
- They are an easy way to print, compare, and order data.
- You can create data that's read-only.

# Example

The example implements a `Person` class that stores some personal information about a person. The `before.py` sample begins with a regular class, which will then be converted into a Dataclass.

```python
class Person:
    name: str
    job: str
    age: str

    def __init__(self, name: str, job: str, age: str) -> None:
        self.name = name
        self.job = job
        self.age = age

person1 = Person("Alice", "Engineer", "30")
person2 = Person("Charlie", "Manager", "30")
person3 = Person("Charlie", "Manager", "40")

print(person1)  # <__main__.Person object at 0x...>
print(id(person2))  # <memory_address>
print(id(person3))  # <different_memory_address>

# Hmm, these should be equal!!!
print(person3 == person2)  # False
```

When executed, the following output is generated.

```sh
<__main__.Person object at 0x000001F0ACC08980>
2133202094672
2133202094992
False
```

Printing `person1` doesn't yield any useful information. You would also expect `person1` and `person2` to be equal since they have the exact same values.

This behavior is typical in regular classes. With Dataclasses, you would prefer these behaviors provide more use.

**Scenarios:**

- *Initializing Data*

    They have a built-in initializer that helps you fill in objects very quickly.

- *Printing Data*

    Dataclasses make it very easy to print the contents of Classes.

- *Comparing Data*

    With data, you may sometimes want to do deeper comparisons, where you take into account multiple `Class` attributes. Also, if the data is the same, you would expect the objects to be the same.

Dataclasses address the problems in the above scenarios.

1. To convert this `Class` into a Dataclass, first you import the dataclass module.

    ```python
    from dataclasses import dataclass
    ```

2. Decorate the class with the `@dataclass` decorator.

    ```python
    @dataclass
    class Person:
        name: str
        job: str
        age: str
    ```

3. There is a built-in initializer helps you fill in objects very quickly, eliminating the need for an `__init__` function, so remove it.

    ```python
    @dataclass
    class Person:
        name: str
        job: str
        age: str

    person1 = Person("Alice", "Engineer", "30")
    person2 = Person("Charlie", "Manager", "30")
    person3 = Person("Charlie", "Manager", "40")
    ```

    This already makes the code more readable by eliminating unnecessary lines from every `Class` we create.

4. We also receive a different result when executing the same program.

    ```sh
    Person(name='Alice', job='Engineer', age='30')
    1164363942480
    1164363952720
    True
    ```

    Instead of the cryptic memory address, we now receive a more readable representation for **Alice**.

    We are also able to compare two objects correctly, with `person3 == person2` now yielding `True`, meaning the two data items are identical.

5. Dataclasses also make it easier to **sort** or **order** data. This can be achieved by specifying `order=True` in the `@dataclass` decorator.