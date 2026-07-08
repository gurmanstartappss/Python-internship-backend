class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Company:
    def __init__(self, employees):
        self.employees = employees


e1 = Employee("Aman", 50000)
e2 = Employee("Gurman", 60000)

c1 = Company([e1, e2])

del c1

print(e1.name, e1.salary)
print(e2.name, e2.salary)   