from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.emp import (EmployeeCreate, EmployeeUpdate, EmployeeResponse)

from app.services.emp import emp_service


router = APIRouter(prefix="/employee")


@router.post("/", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(data: EmployeeCreate, db: Session = Depends(get_db)):
    return emp_service.create_employee(db, data)