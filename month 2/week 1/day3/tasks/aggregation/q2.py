class Book:
    def __init__(self, name):
        self.name = name


class Library:
    def __init__(self, books):
        self.books = books


b1 = Book("Python")
b2 = Book("AI")

l1 = Library([b1, b2])

del l1

print(b1.name)
print(b2.name)