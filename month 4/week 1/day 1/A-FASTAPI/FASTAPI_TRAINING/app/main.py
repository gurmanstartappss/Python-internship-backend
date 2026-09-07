from fastapi import FastAPI
from typing import Optional

from app.schemas.user import UserCreate, Address
from app.database import Base, engine
from app.models.emp import Employee
from app.models.emp import Employee
from app.routers.emp import router as employee_router
app=FastAPI()

app.include_router(employee_router)

@app.get("/")
def home():
    return {"message":"Hello FastAPI"}


@app.get("/users/")
def get_user(name:str,age:int):
    return {"name":name,"age":age}


@app.post("/users")
def create_user(user:UserCreate):
    return{
        "message":"user received successfully",
        "user":user.model_dump()
    }

@app.put("/users/1")
def update_user():
    return {"message":"update user"}


@app.delete("/users/1")
def delete_user():
    return {"message":"delete user"}


#two type of server: Unicorn(FastAPI)ASGI, Django(gunicorn)WSGI
#ASGI
#WSGI
#To run:- uvicorn app.main:app --reload