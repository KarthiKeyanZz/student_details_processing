from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..config import SessionLocal
from .. import schemas, services, crud

router = APIRouter(prefix="/students", tags=["Students"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.StudentResponse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return services.create_student_service(db, student)

@router.post("/bulk", response_model=list[schemas.StudentResponse])
def create_multiple_students(data: schemas.StudentsList, db: Session = Depends(get_db)):
    return services.create_multiple_students_service(db, data.students)

@router.get("/", response_model=list[schemas.StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return crud.get_all_students(db)

@router.get("/{student_id}", response_model=schemas.StudentResponse)
def get_student_by_id(student_id: int, db: Session = Depends(get_db)):
    return services.get_student_by_id_service(db, student_id)


@router.put("/{student_id}", response_model=schemas.StudentResponse)
def update_student(student_id: int, student: schemas.StudentUpdate, db: Session = Depends(get_db)):
    return services.update_student_service(db, student_id, student)

@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return services.delete_student_service(db, student_id)


