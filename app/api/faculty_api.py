from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.faculty_service import FacultyService
from app.models.faculty import Faculty


router = APIRouter(
    prefix="/faculty",
    tags=["Faculty"]
)


class FacultyCreate(BaseModel):
    faculty_id: str
    name: str
    age: int
    email: str
    department: str


@router.get("/")
def get_faculty():

    service = FacultyService()

    faculty_list = service.list_faculty()

    result = []

    for faculty in faculty_list:
        result.append({
            "faculty_id": faculty.faculty_id,
            "name": faculty.name,
            "age": faculty.age,
            "email": faculty.email,
            "department": faculty.department
        })

    return result


@router.get("/{faculty_id}")
def get_one_faculty(faculty_id: str):

    service = FacultyService()

    faculty_list = service.list_faculty()

    for faculty in faculty_list:

        if faculty.faculty_id == faculty_id:

            return {
                "faculty_id": faculty.faculty_id,
                "name": faculty.name,
                "age": faculty.age,
                "email": faculty.email,
                "department": faculty.department
            }

    raise HTTPException(
        status_code=404,
        detail="Faculty not found"
    )


@router.post("/")
def add_faculty(faculty: FacultyCreate):

    service = FacultyService()

    new_faculty = Faculty(
        faculty.faculty_id,
        faculty.name,
        faculty.age,
        faculty.email,
        faculty.department
    )

    service.add_faculty(new_faculty)

    return {
        "faculty_id": new_faculty.faculty_id,
        "name": new_faculty.name,
        "age": new_faculty.age,
        "email": new_faculty.email,
        "department": new_faculty.department
    }


@router.put("/{faculty_id}")
def update_faculty(
    faculty_id: str,
    faculty: FacultyCreate
):

    service = FacultyService()

    faculty_list = service.list_faculty()

    existing_faculty = None

    for item in faculty_list:

        if item.faculty_id == faculty_id:
            existing_faculty = item
            break

    if not existing_faculty:

        raise HTTPException(
            status_code=404,
            detail="Faculty not found"
        )

    service.update_faculty(
        faculty_id,
        name=faculty.name,
        age=faculty.age,
        email=faculty.email,
        department=faculty.department
    )

    return {
        "faculty_id": faculty_id,
        "name": faculty.name,
        "age": faculty.age,
        "email": faculty.email,
        "department": faculty.department
    }


@router.delete("/{faculty_id}")
def delete_faculty(faculty_id: str):

    service = FacultyService()

    faculty_list = service.list_faculty()

    faculty_exists = False

    for faculty in faculty_list:

        if faculty.faculty_id == faculty_id:
            faculty_exists = True
            break

    if not faculty_exists:

        raise HTTPException(
            status_code=404,
            detail="Faculty not found"
        )

    service.remove_faculty(faculty_id)

    return {
        "message": "Faculty deleted successfully"
    }