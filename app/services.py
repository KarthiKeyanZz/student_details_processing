from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from . import crud, schemas, models
from .exceptions import StudentNotFoundException

def create_student_service(db: Session, student: schemas.StudentCreate):
    existing = db.query(models.Student).filter_by(email=student.email).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Email already registered")
    return crud.create_student(db, student)

def update_student_service(db: Session, student_id: int, student: schemas.StudentUpdate):
    updated = crud.update_student(db, student_id, student)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Student not found")
    return updated

def delete_student_service(db: Session, student_id: int):
    success = crud.delete_student(db, student_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Student not found")
    return {"message": "Student deleted successfully"}



def get_student_by_id_service(db: Session, student_id: int):
    student = crud.get_student_by_id(db, student_id)
    if not student:
        raise StudentNotFoundException(student_id)
    return student

def create_multiple_students_service(db: Session, students: list[schemas.StudentCreate]):
    # Optional: Check for duplicate emails before inserting
    existing_emails = [s.email for s in db.query(models.Student).all()]
    for s in students:
        if s.email in existing_emails:
            raise HTTPException(status_code=400, detail=f"Email '{s.email}' already exists.")
    return crud.create_multiple_students(db, students)
