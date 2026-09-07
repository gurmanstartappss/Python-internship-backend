from typing import List,Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.emp import Employee

class employeeRepository:
    def creat(self,db:Session,employee:Employee):
        db.add(employee)
        db.commit()
        db.refresh(employee)
        
        return employee
    
    def get_all(self,db:Session,)->List[Employee]:
        result = db.execute(select(Employee))
        return list[result.scalars().all()]
    
    def get_by_id(self,db: Session,employee_id:int)->Optional[Employee]:
        return db.get(Employee,employee_id)
    
    def update(self,db:Session,employee:Employee)->Employee:
        db.commit()
        db.refresh(employee)
        return employee
    
    def delete(self,db:Session,employee:Employee,)->None:
        db.delete(employee)
        db.refresh(employee)
        return employee