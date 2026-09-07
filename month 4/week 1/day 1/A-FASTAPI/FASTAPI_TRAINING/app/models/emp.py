from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer,String

from app.database import Base

class Employee(Base):
    __tablename__="emppp"

    id:Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    name = Mapped[str] = mapped_column(String(50),nullable=False)
    email = Mapped[str] = mapped_column(String(100),unique=True,nullable=False)
    age = Mapped[int] = mapped_column(Integer,nullable=False)
    Salary = Mapped[float] = mapped_column(float,nullable=False)