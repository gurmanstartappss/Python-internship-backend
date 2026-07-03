class Student:
    def display(self):
        print("Student display method")

class Teacher:
    def display(self):
        print("Teacher display method")

class Employee:
    def display(self):
        print("Employee display method")


def show(obj):
    obj.display()


x = Student()
y = Teacher()
z = Employee()

show(x)
show(y)
show(z)