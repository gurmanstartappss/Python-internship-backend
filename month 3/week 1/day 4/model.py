from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class Department(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

    employees = relationship("EmployeeDetails", back_populates="department")


class EmployeeDetails(Base):
    __tablename__ = "employeeDetails"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    city = Column(String(50))
    branch = Column(String(50))
    designation = Column(String(50))

    department_id = Column(Integer, ForeignKey("department.id"))

    department = relationship("Department", back_populates="employees")