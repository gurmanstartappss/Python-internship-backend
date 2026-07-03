class University():
    def __init__(self,cname):
        self.cname=cname
        print("Student's University name is ",cname)
class Department(University):
    def __init__(self,dept,cname):
        self.dept=dept
        super().__init__(cname)
        print("Student's Department is ",dept)
class Student(Department):
    def __init__(self,name,dept,cname):
        self.name=name
        super().__init__(dept,cname)
        print("Student's Name is ",name)
    def show(self):
        print("Name:", self.name)
        print("Department:", self.dept)
        print("University:", self.cname)

        
        
x=Student("gurman","Mca","CU")
x.show()