from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.student_service import StudentService
from app.models.student import Student


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


class StudentCreate(BaseModel):
    student_id: str
    name: str
    age: int
    email: str
    department: str


@router.get("/")
def get_students():

    service = StudentService()

    students = service.list_students()

    result = []

    for student in students:
        result.append({
            "student_id": student.student_id,
            "name": student.name,
            "age": student.age,
            "email": student.email,
            "department": student.department
        })

    return result


@router.get("/{student_id}")
def get_student(student_id: str):

    service = StudentService()

    students = service.list_students()

    for student in students:

        if student.student_id == student_id:

            return {
                "student_id": student.student_id,
                "name": student.name,
                "age": student.age,
                "email": student.email,
                "department": student.department
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


@router.post("/")
def add_student(student: StudentCreate):

    service = StudentService()

    new_student = Student(
        student.student_id,
        student.name,
        student.age,
        student.email,
        student.department
    )

    service.add_student(new_student)

    return {
        "student_id": new_student.student_id,
        "name": new_student.name,
        "age": new_student.age,
        "email": new_student.email,
        "department": new_student.department
    }


@router.put("/{student_id}")
def update_student(
    student_id: str,
    student: StudentCreate
):

    service = StudentService()

    students = service.list_students()

    existing_student = None

    for item in students:
        if item.student_id == student_id:
            existing_student = item
            break

    if not existing_student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    service.update_student(
        student_id,
        name=student.name,
        age=student.age,
        email=student.email,
        department=student.department
    )

    return {
        "student_id": student_id,
        "name": student.name,
        "age": student.age,
        "email": student.email,
        "department": student.department
    }


@router.delete("/{student_id}")
def delete_student(student_id: str):

    service = StudentService()

    students = service.list_students()

    student_exists = False

    for student in students:
        if student.student_id == student_id:
            student_exists = True
            break

    if not student_exists:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    service.remove_student(student_id)

    return {
        "message": "Student deleted successfully"
    }