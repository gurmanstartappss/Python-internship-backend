class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.done = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.done:
            raise StopIteration

        self.done = True

        if self.age > 18:
            return "welcome"
        else:
            return "not welcome"


x = Student("gurman", 22)

print(next(x))