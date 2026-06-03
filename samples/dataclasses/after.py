from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        object.__setattr__(self, "sort_index", (self.age, self.name, self.job))


person1 = Person("Alice", "Engineer", 30, 80)
person2 = Person("Charlie", "Manager", 40)
person3 = Person("Charlie", "Manager", 40)

print(person1)  # Person(name='Alice', job='Engineer', age=30, strength=80)
print(id(person2))  # <memory_address>
print(id(person3))  # <different_memory_address>

# Hmm, these are now equal!!!
print(person3 == person2)  # True

# Need to specify what this means
print(person1 < person2)  # Now we can compare them
