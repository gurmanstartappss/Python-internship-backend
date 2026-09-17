# S

def get_employee(employee_type):
    if employee_type == "permanent":
        return PermanentEmployee()

    elif employee_type == "contract":
        return ContractEmployee()

    elif employee_type == "intern":
        return InternEmployee()

    else:
        raise ValueError("Invalid employee type")



# O
class Employee:
    def calculate_salary(self):
        pass


class PermanentEmployee(Employee):
    def calculate_salary(self):
        return 40000


class ContractEmployee(Employee):
    def calculate_salary(self):
        return 30000


class InternEmployee(Employee):
    def calculate_salary(self):
        return 15000
        
class FreelancerEmployee(Employee):
    def calculate_salary(self):
        return 10000