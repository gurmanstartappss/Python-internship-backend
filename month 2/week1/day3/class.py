"""data class-first from dataclasses import dataclass and uses @dataclass before the class 
@dataclass reduces boilerplate code for classes whose main purpose is storing data."""

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    marks: float

s1 = Student("Gurman", 22, 85.5)

print(s1)