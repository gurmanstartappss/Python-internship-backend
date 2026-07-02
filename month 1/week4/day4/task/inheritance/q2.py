class Person():
    def breath(self):
        print("Person is breathing ")
class Employee(Person):
    def work(self):
        print("Employee is working ")
        super().breath()
class Manager(Employee):
    def manage(self):
        print("Manager is managing")
        super().work()

x=Manager()
x.manage()


"""
or 
"""

class Person():
    def breath(self):
        print("Person is breathing ")
class Employee(Person):
    def work(self):
        print("Employee is working ")
class Manager(Employee):
    def manage(self):
        print("Manager is managing")

x=Manager()
x.manage()
x.work()
x.breath()
