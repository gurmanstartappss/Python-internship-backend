class Employee:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def work(self):
        return self.__name,self.__age
x=Employee("Gurman",22)
print(x.work())
print("------------------")

class Student:
    college="CU"
    def __init__(self,roll,marks):
        self.roll_no=roll
        self.__marks=marks
        
    def roll(self):
        return self.roll_no
    
    def get(self):
        return self.__marks
    
    def set(self,x):
        self.__marks=x
    
    @property
    def result(self):
        if self.__marks>=40:
            return ("Pass")
        else:
            return ("Fail")
            
obj1=Student(101,55)
obj2=Student(102,33)
print("student 1 marks:-", obj1.get())
print("student 2 marks:-", obj2.get())
obj2.set(99)
print("student 2 marks:-", obj2.get())
print(obj1.result)
print(obj2.result)
print(obj1.roll())
print(Student.college)