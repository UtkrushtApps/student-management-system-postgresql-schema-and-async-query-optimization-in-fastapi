from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.database import get_connection
from app.schemas.schemas import Student, Course, Enrollment

router = APIRouter()

@router.get("/students", response_model=List[Student])
def list_students():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, name, email FROM students")
        rows = cur.fetchall()
        return [Student(id=row[0], name=row[1], email=row[2]) for row in rows]
    finally:
        conn.close()

@router.get("/courses", response_model=List[Course])
def list_courses():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, name, description FROM courses")
        rows = cur.fetchall()
        return [Course(id=row[0], name=row[1], description=row[2]) for row in rows]
    finally:
        conn.close()

@router.get("/courses/{course_id}/students", response_model=List[Student])
def students_by_course(course_id: int, status: Optional[str] = Query(None)):
    conn = get_connection()
    try:
        cur = conn.cursor()
        # Inefficient LEFT JOIN and filtering implementation
        query = """
        SELECT s.id, s.name, s.email FROM students s
        LEFT JOIN enrollments e ON s.id = e.student_id
        WHERE e.course_id = %s
        """
        params = [course_id]
        if status:
            query += " AND e.status = '%s'" % (status,)
        cur.execute(query, params)
        rows = cur.fetchall()
        return [Student(id=row[0], name=row[1], email=row[2]) for row in rows]
    finally:
        conn.close()

@router.get("/enrollments", response_model=List[Enrollment])
def list_enrollments():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, student_id, course_id, status FROM enrollments")
        rows = cur.fetchall()
        return [Enrollment(id=row[0], student_id=row[1], course_id=row[2], status=row[3]) for row in rows]
    finally:
        conn.close()
