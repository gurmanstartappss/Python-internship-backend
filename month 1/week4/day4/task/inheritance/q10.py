class Shape:
    def common(self):
        print("This is a shape")


class Rectangle(Shape):
    def rectangle(self):
        print("This is a rectangle")


class Circle(Shape):
    def circle(self):
        print("This is a circle")


class Triangle(Shape):
    def triangle(self):
        print("This is a triangle")


x = Rectangle()
y = Circle()
z = Triangle()

x.rectangle()
x.common()

y.circle()
y.common()

z.triangle()
z.common()