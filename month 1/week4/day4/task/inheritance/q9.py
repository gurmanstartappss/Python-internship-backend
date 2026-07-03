class University:
    def __init__(self, uname):
        self.uname = uname
        print("Student belongs to", uname)


class Degree(University):
    def __init__(self, uname, deg):
        self.deg = deg
        super().__init__(uname)
        print("Student Degree is", deg)


class Sports:
    def __init__(self, sports):
        self.sports = sports
        print("Student Sports is", sports)


class Student(Degree, Sports):
    def __init__(self, uname, deg, name, sports):
        self.name = name

        Degree.__init__(self, uname, deg)
        Sports.__init__(self, sports)

        print("Student name is", name)

    def show(self):
        print(self.uname, self.deg, self.name, self.sports)


x = Student("CU", "MCA", "Gurman", "Football")
x.show()

print(Student.mro())