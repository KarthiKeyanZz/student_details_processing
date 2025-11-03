from fastapi import FastAPI
from .config import Base, engine
from .api import routes_students
from .exceptions import register_exception_handlers

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Student Details Processing API")

# Include routes
app.include_router(routes_students.router)

# Register exception handlers
register_exception_handlers(app)
