from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Area of Circle")

class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle")

c = Circle()
r = Rectangle()

c.area()
r.area()