from fastapi import HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from app.models.emp import Employee
from app.repository.emp import EmployeeRepository
from app.schemas.emp import EmployeeCreate, EmployeeResponse, EmployeeUpdate
from app.exceptions import EmployeeNotFoundException

class EmployeeService:

    def __init__(self, repository: EmployeeRepository):
        self.repository = repository

    def create_employee(
        self,
        db: Session,
        data: EmployeeCreate
    ) -> Employee:

        existing_employee = self.repository.get_by_email(
            db,
            data.email
        )

        if existing_employee:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Employee with this email already exists"
            )

        employee = Employee(
            name=data.name,
            email=data.email,
            age=data.age,
            salary=data.salary
        )

        return self.repository.create(db, employee)

    def get_all_employee(
        self,
        db: Session
    ) -> List[Employee]:

        return self.repository.get_all(db)

    def get_employee(
        self,
        db: Session,
        employee_id: int
    ) -> Employee:

        existing_employee = self.repository.get_by_id(
            db,
            employee_id
        )

        if not existing_employee:
            raise EmployeeNotFoundException(employee_id)

        return existing_employee


emp_repo = EmployeeRepository()
emp_service = EmployeeService(emp_repo)