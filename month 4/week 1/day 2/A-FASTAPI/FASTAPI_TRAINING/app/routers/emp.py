from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.emp import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse
)
from app.services.emp import emp_service


router = APIRouter(prefix="/employee")


@router.post(
    "/",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED
)
def create_employee(
    data: EmployeeCreate,
    db: Session = Depends(get_db)
):
    return emp_service.create_employee(db, data)


@router.get(
    "/",
    response_model=List[EmployeeResponse]
)
def get_employees(
    db: Session = Depends(get_db)
):
    return emp_service.get_all_employee(db)


@router.get(
    "/{employee_id}",
    response_model=EmployeeResponse
)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    return emp_service.get_employee(db, employee_id)