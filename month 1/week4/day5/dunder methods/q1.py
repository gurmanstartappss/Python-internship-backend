class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return (f"Name-{self.name} , Age-{self.age}")
emp1=Employee("gurman",21)
print(emp1)