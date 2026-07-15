from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    price: float


b1 = Book("Python Basics", "John", 500)

print(b1)