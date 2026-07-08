class Student():
    def __init__(self,name):
        self.name=name

class Teacher():
    def __init__(self,tname):
        self.tname=tname
        
    def teach(self,students):
        for student in students:
            print(self.tname, "teaches", student.name)
            
s1 = Student("Aman")
s2 = Student("Rahul")
s3 = Student("Gurman")
t1 = Teacher("Mr. Sharma")

t1.teach([s1, s2, s3])