#normal and parameterised query

# pip install sqlalchemy psycopg[binary]
# SQLAlchemy: it is a Python toolkit to communicate with a database

# 1. SQLAlchemy Core (row query)
# 2. SQLAlchemy ORM (communicate by Python objects)


#ORM
# ORM methods
#pip install alembic
# for initializing=alembic init alembic
#alembic:=its sqlalchemy's migration tool it tracks database 
# and schema changes and updates the db without losing existing
#make migrations= alembic revision --autogenerate -m "add salary column in employee table"
#alembic upgrade head
from db import Base, engine, SessionLocal
from model import EmployeeDetails, Department

Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Create Department
dept = Department(name="IT")

db.add(dept)
db.commit()
db.refresh(dept)


# Create Employee with department
employee = EmployeeDetails(
    name="gurman",
    city="indore",
    branch="indore",
    designation="python developer",
    department_id=dept.id
)

db.add(employee)
db.commit()
db.refresh(employee)


# Read data
emp = db.query(EmployeeDetails).all()

for e in emp:
    print(
        e.id,
        e.name,
        e.city,
        e.branch,
        e.designation,
        e.department.name
    )




emp=db.query(EmployeeDetails).filter(EmployeeDetails.id==1).first()
emp.city="bhopal"
db.commit()
print(emp)
db.close()
# orm methods

