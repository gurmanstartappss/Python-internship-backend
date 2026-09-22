from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional


class EmployeeCreate(BaseModel):

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid"
    )

    name: str = Field(
        min_length=3,
        max_length=50,
        description="Employee full name"
    )

    age: int = Field(
        ge=0,
        le=60
    )

    email: str

    salary: float = Field(
        gt=0
    )

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        value = value.strip()

        if not value.replace(" ", "").isalpha():
            raise ValueError("Name must contain only letters")

        return value

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        value = value.strip().lower()

        if not value.endswith("@gmail.com"):
            raise ValueError("only gmail addresses are allowed")

        return value


class EmployeeUpdate(BaseModel):

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid"
    )

    name: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=50
    )

    age: Optional[int] = Field(
        default=None,
        ge=0,
        le=60
    )

    email: Optional[str] = None

    salary: Optional[float] = Field(
        default=None,
        gt=0
    )

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if value is None:
            return value

        value = value.strip()

        if not value.replace(" ", "").isalpha():
            raise ValueError("Name must contain only letters")

        return value

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        if value is None:
            return value

        value = value.strip().lower()

        if not value.endswith("@gmail.com"):
            raise ValueError("only gmail addresses are allowed")

        return value


class EmployeeResponse(BaseModel):

    id: int
    name: str
    email: str
    age: int
    salary: float

    model_config = ConfigDict(
        from_attributes=True
    )