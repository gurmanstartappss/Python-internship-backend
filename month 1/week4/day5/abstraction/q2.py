from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Full-time salary is 50000")

class Freelancer(Employee):
    def calculate_salary(self):
        print("Freelancer salary is 30000")

f = FullTimeEmployee()
fr = Freelancer()

f.calculate_salary()
fr.calculate_salary()