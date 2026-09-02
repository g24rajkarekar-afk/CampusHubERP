from fastapi import FastAPI

from app.api.student_api import router as student_router
from app.api.faculty_api import router as faculty_router
from app.api.course_api import router as course_router
from app.api.enrollment_api import router as enrollment_router


app = FastAPI(
    title="CampusHub ERP API",
    description="REST API for CampusHub ERP",
    version="1.0.0"
)


app.include_router(student_router)
app.include_router(faculty_router)
app.include_router(course_router)
app.include_router(enrollment_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to CampusHub ERP API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "API is running"
    }