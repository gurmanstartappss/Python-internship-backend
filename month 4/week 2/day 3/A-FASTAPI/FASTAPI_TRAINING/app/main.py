from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.middleware import log_request
from app.database import Base, engine
from app.models.emp import Employee
from app.routers.emp import router as employee_router
from app.dependencies import get_current_user
from app.exception_handlers import employee_not_found_handler
from app.exceptions import EmployeeNotFoundException

app = FastAPI()

app.middleware("http")(log_request)

Base.metadata.create_all(bind=engine)

app.include_router(employee_router)

app.add_exception_handler(EmployeeNotFoundException,employee_not_found_handler)

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}


@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    if form_data.username != "root" or form_data.password != "root":
        raise HTTPException(
            status_code=401,
            detail="Wrong username or password"
        )

    return {
        "access_token": "root",
        "token_type": "bearer"
    }


# Protected test route
@app.get("/protected")
def protected(
    username=Depends(get_current_user)
):
    return {
        "message": "You are authenticated",
        "username": username
    }
    
#two type of server: Uvicorn(FastAPI)ASGI, Django(gunicorn)WSGI
#ASGI
#WSGI
#To run:- uvicorn app.main:app --reload