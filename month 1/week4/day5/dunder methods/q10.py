class Student:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        return "Welcome " + self.name


x = Student("Gurman")

print(x())