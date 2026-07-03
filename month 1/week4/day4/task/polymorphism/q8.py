class Shape:
    def area(self):
        print("Area of shape")


class Rectangle(Shape):
    def area(self):
        length = 10
        width = 5
        print("Area of Rectangle:", length * width)


class Circle(Shape):
    def area(self):
        radius = 7
        print("Area of Circle:", 3.14 * radius * radius)


class Square(Shape):
    def area(self):
        side = 4
        print("Area of Square:", side * side)


def display_area(shape):
    shape.area()


x = Rectangle()
y = Circle()
z = Square()

display_area(x)
display_area(y)
display_area(z)