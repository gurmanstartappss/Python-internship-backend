class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def __lt__(self,other):
        return self.salary<other.salary
                                                                                            


e1 = Employee("Aman", 50000)
e2 = Employee("Rahul", 60000)
print(e1 < e2)   # True
print(e2 < e1)   # False