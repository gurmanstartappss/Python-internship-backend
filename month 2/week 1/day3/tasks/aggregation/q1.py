class Employee:
    def __init__(self, name):
        self.name = name
class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def show(self):
        for employee in self.employees:
            print(self.name, "has employee",employee.name)
        

e1 = Employee("Aman")
e2 = Employee("Gurman")

d1 = Department("IT", [e1, e2])
Department.show(d1)