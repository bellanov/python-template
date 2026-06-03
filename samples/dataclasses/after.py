from dataclasses import dataclass

@dataclass(order=True)
class Person:
    name: str
    job: str
    age: str

person1 = Person("Alice", "Engineer", "30")
person2 = Person("Charlie", "Manager", "40")
person3 = Person("Charlie", "Manager", "40")

print(person1)  # Person(name='Alice', job='Engineer', age='30')
print(id(person2))  # <memory_address>
print(id(person3))  # <different_memory_address>

# Hmm, these should be equal!!!
print(person3 == person2)  # True

# Need to specify what this means
print(person3 > person2)
print(person3 < person2)
print(person3 >= person2)
print(person3 <= person2)