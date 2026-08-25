from fastapi import FastAPI
from app.schemas.users import UserCreate,Address

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello FastAPI"}


@app.get("/users/{name}")
def get_user(name: str, age: int):
    return {
        "name": name,
        "age": age
    }


@app.post("/users")
def create_user(user: UserCreate):
    return {
        "message": "User received successfully",
        "user": user.model_dump()
    }


@app.put("/users/1")
def update_user():
    return {"message": "Update User"}


@app.delete("/users/1")
def delete_user():
    return {"message": "Delete User"}