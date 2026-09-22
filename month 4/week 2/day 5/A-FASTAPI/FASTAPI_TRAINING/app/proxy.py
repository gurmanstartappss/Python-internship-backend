from abc import ABC, abstractmethod


# Abstract Class
class EmployeeService(ABC):

    @abstractmethod
    def get_employee(self, employee_id):
        pass


# Real Subject
class AuthenticEmployeeService(EmployeeService):

    def get_employee(self, employee_id):
        print("Fetching employee from database.....")

        return {
            "id": employee_id,
            "name": "abc",
            "department": "engineer",
            "age": 22
        }


# Proxy
class EmployeeProxy(EmployeeService):

    def __init__(self):
        self.employee_service = None

    def get_employee(self, employee_id):
        print("Proxy: Checking employee request...")

        # Lazy initialization
        if self.employee_service is None:
            self.employee_service = AuthenticEmployeeService()

        return self.employee_service.get_employee(employee_id)


# Client
employee = EmployeeProxy()

result = employee.get_employee(101)

print(result)