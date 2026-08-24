from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name:str
    age:int
    email:str

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

@app.get("/users/{name}")#path parameter curly braces
def get_user(name: str, age : int):
    return {"name":name,"age":age}

@app.post("/users")
def create_user(user:UserCreate):#query parameters
    return user

@app.put("/users/1")
def update_user():
    return {"message": "Update Users"}

@app.delete("/users/1")
def delete_user():
    return {"message": "Get Users"}

#type hints: user for validation,documentation,request parsing 
