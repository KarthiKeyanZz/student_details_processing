from pydantic import BaseModel, EmailStr
from typing import List

class StudentBase(BaseModel):
    name: str
    email: EmailStr
    course: str

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int

    class Config:
        orm_mode = True


class StudentsList(BaseModel):
    students: List[StudentCreate]
