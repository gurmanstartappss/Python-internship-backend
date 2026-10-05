from fastapi import HTTPException, status


class EmployeeNotFoundException(HTTPException):
    def __init__(self, employee_id: int):
        print(employee_id)
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with Id {employee_id} was not found."
        )
        
