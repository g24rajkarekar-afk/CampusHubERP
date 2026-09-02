from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.enrollment_service import EnrollmentService

router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)


class EnrollmentCreate(BaseModel):
    student_id: str
    course_code: str


@router.get("/")
def get_enrollments():

    service = EnrollmentService()
    enrollments = service.list_enrollments()

    result = []

    for enrollment in enrollments:
        result.append({
            "enrollment_id": enrollment.enrollment_id,
            "student_id": enrollment.student_id,
            "course_code": enrollment.course_code
        })

    return result


@router.post("/")
def add_enrollment(enrollment: EnrollmentCreate):

    service = EnrollmentService()

    new_enrollment = service.add_enrollment(
        enrollment.student_id,
        enrollment.course_code
    )

    return {
        "enrollment_id": new_enrollment.enrollment_id,
        "student_id": new_enrollment.student_id,
        "course_code": new_enrollment.course_code
    }


@router.delete("/{enrollment_id}")
def delete_enrollment(enrollment_id: int):

    service = EnrollmentService()

    enrollment = service.remove_enrollment(enrollment_id)

    if not enrollment:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return {
        "message": "Enrollment deleted successfully"
    }