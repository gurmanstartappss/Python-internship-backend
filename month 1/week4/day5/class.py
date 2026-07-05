# abstraction in detail 
# ABC: Abstract Base Class
# @abstractmethod: method that must be implemented by child classes
# Abstract Class: it is a blueprint for other class, we can't create its object directly, but child classes can inherit and implement its methods
# ABC: Provided by python to create abstract classes. it defines common rules that all child classes must follow
# @abstractmethod: it is a decorator that declares a method which every child class must implement. A subclass cannot be create object until it provide that method
from abc import ABC, abstractmethod
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog barks")


obj = Dog()
obj.sound()

"""
# Special Methods / Dunder Methods:
# Special methods that start and end with double underscores (__).
# They are defined inside a class.
# Python automatically calls them in certain situations,
# allowing us to customize the behavior of objects.

# Examples:
# 1. __iter__()  -> makes an object iterable
# 2. __new__()   -> creates a new object/instance
# 3. __str__()   -> defines the user-friendly string representation of an object
# 4. __init__()  -> initializes an object after it is created
# 5. __repr__()  -> defines the developer-friendly string representation for debugging
# 6. __len__()   -> defines what len() returns for an object
# 7. __add__() -> defines the behavior of + operator between objects
# 8. __eq__() -> defines the behavior of == operator between objects"""


class Student:

    def __init__(self, name):
        self.full_name = name

    def __str__(self):
        return f"Student name: {self.full_name}"

    def __repr__(self):
        return f"Student('{self.full_name}')"

    def __len__(self):
        return len(self.full_name)

    def __iter__(self):
        return iter(self.full_name)

    def __add__(self, other):
        return self.full_name + other.full_name

    def __eq__(self, other):
        return self.full_name == other.full_name


obj1 = Student("Gurman")
obj2 = Student("Gurman")

# Testing dunder methods
print(obj1)          # calls __str__()
print(repr(obj1))    # calls __repr__()
print(len(obj1))     # calls __len__()

for i in obj1:       # calls __iter__()
    print(i)

print(obj1 + obj2)   # calls __add__()
print(obj1 == obj2)  # calls __eq__()


# Static Method:
# - Does not use self or cls
# - Uses @staticmethod decorator
# - Works like a normal function inside a class
# - Cannot directly access instance or class data

# Class Method:
# - cls is passed as the first parameter
# - Uses @classmethod decorator
# - Works with class-level data
# - Can access and modify class variables 

class Student:

    school = "test"

    def __init__(self, name):
        self.name = name

    @classmethod
    def display(cls, scl_name):
        cls.school = scl_name


obj = Student("abc")

print(obj.name)          # abc

Student.display("demo")  # changes class variable

print(Student.school)    # demo

# Instance Method/normal method is an instance method:
# - self is passed as the first parameter
# - Works with object/instance data
# - Can access and modify instance variables

# __init__ Method:
# - Special/dunder method
# - Automatically called after an object is created
# - Used to initialize object attributes
# - self is passed as the first parameter

