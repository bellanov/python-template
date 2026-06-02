from dataclasses import dataclass

@dataclass
class Person:
    name: str
    job: str
    age: str

person1 = Person("Alice", "Engineer", "30")
person2 = Person("Charlie", "Manager", "30")
person3 = Person("Charlie", "Manager", "40")

print(person1)  # <__main__.Person object at 0x...>
print(id(person2))  # <memory_address>
print(id(person3))  # <different_memory_address>

# Hmm, these should be equal!!!
print(person3 == person2)  # False
