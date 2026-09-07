from pydantic import BaseModel,Field,field_validator,ConfigDict


class Address(BaseModel):
    city:str
    state:str
    pincode:str

class UserCreate(BaseModel):
    model_config=ConfigDict(str_strip_whitespace=True)
    model_config=ConfigDict(extra="forbid")
    name:str =Field(min_length=3, max_length=50,description="Employee full name")
    age:int = Field(ge=0, le=60)
    email:str
    address:Address
    is_active:bool =Field(default=True)


    @field_validator("name")
    @classmethod
    def validate_name(cls,value):
        value=value.strip()
        if len(value)<2:
            raise ValueError("Name must be at least 2 characters long")
        return value
    
    @field_validator("email")
    @classmethod
    def validate_email(cls,value):
        value=value.strip().lower()
        if not value.endswith("@gmail.com"):
            raise ValueError("only gmail addresses are allowed")
        return value

print(UserCreate.model_json_schema)


#ge- greater then or equal to
#le- less than or equal to 