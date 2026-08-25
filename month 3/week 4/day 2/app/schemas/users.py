from pydantic import BaseModel,Field,field_validator,ConfigDict


class Address(BaseModel):
    city: str
    state: str
    pincode: int


class UserCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(
        min_length=3,
        max_length=50,
        description="Employee Fullname"
    )
    age: int = Field(ge=1, le=60)
    email: str
    address: Address
    is_active: bool = Field(default=True)

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        value = value.strip().lower()

        if not value.endswith("@gmail.com"):
            raise ValueError("only gmail addresses are allowed")

        return value
    
    
    @field_validator("name")
    @classmethod
    def  validate_name(cls,value):
        value=value.strip()
        
        if not value.replace("","").isalpha():
            raise ValueError("name must contain only letters and spaces")
        return value

print(UserCreate.model_json_schema())