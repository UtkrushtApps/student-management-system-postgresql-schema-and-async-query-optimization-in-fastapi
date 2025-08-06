from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    email: str

class Course(BaseModel):
    id: int
    name: str
    description: str

class Enrollment(BaseModel):
    id: int
    student_id: int
    course_id: int
    status: str
