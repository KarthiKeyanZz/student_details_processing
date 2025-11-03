from sqlalchemy.orm import Session
from . import models, schemas

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_all_students(db: Session):
    return db.query(models.Student).all()

def create_student(db: Session, student: schemas.StudentCreate):
    new_student = models.Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

def update_student(db: Session, student_id: int, student_data: schemas.StudentUpdate):
    student = get_student(db, student_id)
    if not student:
        return None
    for key, value in student_data.dict().items():
        setattr(student, key, value)
    db.commit()
    db.refresh(student)
    return student

def delete_student(db: Session, student_id: int):
    student = get_student(db, student_id)
    if student:
        db.delete(student)
        db.commit()
        return True
    return False

def get_student_by_id(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def create_multiple_students(db: Session, students: list[schemas.StudentCreate]):
    new_students = [models.Student(**student.dict()) for student in students]
    db.add_all(new_students)
    db.commit()
    for s in new_students:
        db.refresh(s)
    return new_students
