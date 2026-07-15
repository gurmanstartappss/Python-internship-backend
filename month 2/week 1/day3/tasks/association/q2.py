class Patient():
    def __init__(self,name):
        self.name=name
        
class Doctor():
    def __init__(self,pname):
        self.pname=pname
        
    def nurse(self,patients):
        for patient in patients:
            print(self.pname , "attends", patient.name)
        

        

s1 = Patient("Aman")
s2 = Patient("Rahul")
s3 = Patient("Gurman")

t1 = Doctor("Mr. Sharma")


t1.nurse([s1, s2, s3])