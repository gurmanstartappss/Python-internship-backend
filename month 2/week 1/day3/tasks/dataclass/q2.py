from dataclasses import dataclass

@dataclass
class Employee:
    employee_id: int
    name: str
    department: str
    salary: float


e1 = Employee(1, "Aman", "IT", 50000)
e2 = Employee(1, "Aman", "IT", 50000)

print(e1 == e2)