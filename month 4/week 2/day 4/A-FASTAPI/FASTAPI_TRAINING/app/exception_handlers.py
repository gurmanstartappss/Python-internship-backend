from app.exceptions import EmployeeNotFoundException
from fastapi import Request
from fastapi.responses import JSONResponse
import logging

logger=logging.getLogger(__name__)

def employee_not_found_handler(request:Request,exc:EmployeeNotFoundException,):
    return JSONResponse(status_code=404,content={"error":"Employee_not_found","message":(f"Employee {exc.employee_id}""was not found")})