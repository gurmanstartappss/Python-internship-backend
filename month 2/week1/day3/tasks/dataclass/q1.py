from dataclasses import dataclass

@dataclass
class Student:
    id: int
    name: str
    age: int
    course: str


s1 = Student(1, "Gurman", 22, "MCA")

print(s1)