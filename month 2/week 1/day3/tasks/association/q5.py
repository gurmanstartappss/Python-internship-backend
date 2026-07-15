class Trainer:
    def __init__(self, name):
        self.name = name

    def teach(self, courses):
        for course in courses:
            print(self.name, "teaches", course.name)


class Course:
    def __init__(self, name):
        self.name = name


t1 = Trainer("Mr. Sharma")

c1 = Course("Python")
c2 = Course("AI")
c3 = Course("Machine Learning")

t1.teach([c1, c2, c3])