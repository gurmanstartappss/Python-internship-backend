class Teacher:
    def __init__(self, name):
        self.name = name


class School:
    def __init__(self, teachers):
        self.teachers = teachers


t1 = Teacher("Mr. Sharma")
t2 = Teacher("Mr. Singh")

s1 = School([t1, t2])

del s1

print(t1.name)
print(t2.name)