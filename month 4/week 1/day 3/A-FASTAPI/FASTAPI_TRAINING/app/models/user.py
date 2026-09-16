from enum import Enum
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class UserRole(str, Enum):
    ADMIN = "Admin"
    HR = "HR"
    EMPLOYEE="EMPLOYEE"
