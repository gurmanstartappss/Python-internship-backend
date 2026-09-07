from pydantic import BaseModel,Field,field_validator,ConfigDict
from typing import Optional

class EmployeeCreate(BaseModel):
    model_config=ConfigDict(str_strip_whitespace=True)
    model_config=ConfigDict(extra="forbid")
    name:str =Field(min_length=3, max_length=50,description="Employee full name")
    age:int = Field(ge=0, le=60)
    email:str
    Salary:float = Field(gt=0)
    


    @field_validator("name")
    @classmethod
    def validate_name(cls,value):
        value=value.strip()
        if not value.replace(" ","").isalpha():
            raise ValueError("Name must contain only letters")
        return value
    
    @field_validator("email")
    @classmethod
    def validate_email(cls,value):
        value=value.strip().lower()
        if not value.endswith("@gmail.com"):
            raise ValueError("only gmail addresses are allowed")
        return value





class EmployeeUpdate(BaseModel):
    name:Optional[str] =Field(min_length=3, max_length=50,description="Employee full name")
    age:Optional[int] = Field(ge=0, le=60)
    email:Optional[str]
    Salary:Optional[float] = Field(gt=0)
   


    @field_validator("name")
    @classmethod
    def validate_name(cls,value):
        value=value.strip()
        if not value.replace(" ","").isalpha():
            raise ValueError("Name must contain only letters")
        return value
    
    @field_validator("email")
    @classmethod
    def validate_email(cls,value):
        value=value.strip().lower()
        if not value.endswith("@gmail.com"):
            raise ValueError("only gmail addresses are allowed")
        return value

    


class EmployeeResponse(BaseModel):
    id:int
    name:str
    email:str
    age:int
    Salary:float

    model_config = ConfigDict(from_attributes=True)


#from_attributes = True allows pydantic to build the response model from object attribute
#SQLAlchemy employee = pydantic response Model -> JSON