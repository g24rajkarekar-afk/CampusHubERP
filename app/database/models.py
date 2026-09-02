from sqlalchemy import Column, Integer, String
from app.database.db import Base


class StudentDB(Base):
    __tablename__ = "students"

    student_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, nullable=False)
    department = Column(String, nullable=False)


class FacultyDB(Base):
    __tablename__ = "faculty"

    faculty_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, nullable=False)
    department = Column(String, nullable=False)


class CourseDB(Base):
    __tablename__ = "courses"

    course_code = Column(String, primary_key=True)
    course_name = Column(String, nullable=False)
    credits = Column(Integer, nullable=False)


class EnrollmentDB(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(String, nullable=False)
    course_code = Column(String, nullable=False)