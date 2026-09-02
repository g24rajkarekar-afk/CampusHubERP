from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.course_service import CourseService
from app.models.course import Course


router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


class CourseCreate(BaseModel):
    course_code: str
    course_name: str
    credits: int


@router.get("/")
def get_courses():

    service = CourseService()

    courses = service.list_courses()

    result = []

    for course in courses:
        result.append({
            "course_code": course.course_code,
            "course_name": course.course_name,
            "credits": course.credits
        })

    return result


@router.get("/{course_code}")
def get_one_course(course_code: str):

    service = CourseService()

    courses = service.list_courses()

    for course in courses:

        if course.course_code == course_code:

            return {
                "course_code": course.course_code,
                "course_name": course.course_name,
                "credits": course.credits
            }

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )


@router.post("/")
def add_course(course: CourseCreate):

    service = CourseService()

    new_course = Course(
        course.course_code,
        course.course_name,
        course.credits
    )

    service.add_course(new_course)

    return {
        "course_code": new_course.course_code,
        "course_name": new_course.course_name,
        "credits": new_course.credits
    }


@router.put("/{course_code}")
def update_course(
    course_code: str,
    course: CourseCreate
):

    service = CourseService()

    courses = service.list_courses()

    existing_course = None

    for item in courses:

        if item.course_code == course_code:
            existing_course = item
            break

    if not existing_course:

        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    service.update_course(
        course_code,
        course_name=course.course_name,
        credits=course.credits
    )

    return {
        "course_code": course_code,
        "course_name": course.course_name,
        "credits": course.credits
    }


@router.delete("/{course_code}")
def delete_course(course_code: str):

    service = CourseService()

    courses = service.list_courses()

    course_exists = False

    for course in courses:

        if course.course_code == course_code:
            course_exists = True
            break

    if not course_exists:

        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    service.remove_course(course_code)

    return {
        "message": "Course deleted successfully"
    }