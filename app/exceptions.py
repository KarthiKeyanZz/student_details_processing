from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

# Custom Exception Classes
class StudentNotFoundException(HTTPException):
    def __init__(self, student_id: int):
        super().__init__(
            status_code=404,
            detail=f"Student with ID {student_id} not found."
        )

class EmailAlreadyExistsException(HTTPException):
    def __init__(self, email: str):
        super().__init__(
            status_code=400,
            detail=f"The email '{email}' is already registered."
        )


# Global Exception Handlers (used by FastAPI)
def register_exception_handlers(app):

    @app.exception_handler(IntegrityError)
    async def integrity_error_handler(request: Request, exc: IntegrityError):
        return JSONResponse(
            status_code=400,
            content={"error": "Database integrity error (possible duplicate or invalid entry)."}
        )

    @app.exception_handler(SQLAlchemyError)
    async def sqlalchemy_error_handler(request: Request, exc: SQLAlchemyError):
        return JSONResponse(
            status_code=500,
            content={"error": "A database error occurred.", "details": str(exc)}
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"error": "An unexpected error occurred.", "details": str(exc)}
        )
