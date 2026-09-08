from fastapi import FastAPI

from app.database import Base, engine
from app.models.emp import Employee
from app.routers.emp import router as employee_router


app = FastAPI() 

Base.metadata.create_all(bind=engine)

app.include_router(employee_router)


@app.get("/")
def home():
    return {"message": "Hello FastAPI"}
#two type of server: Uvicorn(FastAPI)ASGI, Django(gunicorn)WSGI
#ASGI
#WSGI
#To run:- uvicorn app.main:app --reload