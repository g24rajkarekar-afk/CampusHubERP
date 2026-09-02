from app.database.db import engine, SessionLocal, Base
from app.database import models
from app.database.models import StudentDB
from app.utils.iterators import StudentIterator
from app.utils.generators import (id_generator,student_report,faculty_report,course_report)
from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course
from app.services.student_service import StudentService
from app.services.faculty_service import FacultyService
from app.services.course_service import CourseService
from app.utils.threading_tasks import generate_reports_concurrently
from app.utils.multiprocessing_tasks import compare_execution
from app.utils.async_tasks import run_async_reports
import asyncio
from app.utils.api_tasks import fetch_multiple_apis
from app.services.async_service import load_all_data
from app.services.async_service import load_all_data, generate_all_reports
from app.utils.serializers import (save_student_json,load_student_json,save_courses_json,load_courses_json)
from app.utils.validators import validate_email, validate_student_id
from app.utils.csv_manager import (export_students_csv,import_students_csv)
from app.utils.pickle_manager import (save_students_pickle,load_students_pickle)
from app.utils.module_loader import load_module

student = Student(
    "ST001",
    "Raj Karekar",
    20,
    "raj@gmail.com",
    "Computer Science"
)

faculty = Faculty(
    "FC001",
    "Radhika Ahuja",
    35,
    "radhika@gmail.com",
    "Computer Science"
)

course = Course(
    "CS101",
    "Python Programming",
    4
)


print("\n--- STUDENT ---")
student.display_details()

print("\n--- FACULTY ---")
faculty.display_details()

print("\n--- COURSE ---")
course.display_details()

print("\n--- TESTING NAME VALIDATION ---")

try:
    student.name = ""
except ValueError as e:
    print("Error:", e)

print("\n--- TESTING EMAIL VALIDATION ---")

try:
    student.email = "rajgmail.com"
except ValueError as e:
    print("Error:", e)

print("\n--- TESTING AGE VALIDATION ---")

try:
    student.age = 10
except ValueError as e:
    print("Error:", e)

print("\n--- TESTING METACLASS ---")

print("Created At:", student.created_at)
print("Updated At:", student.updated_at)

print("\n--- TESTING TO_DICT ---")

print(student.to_dict())

print("\n--- WEEK 2 SERVICE TESTING ---")

student_service = StudentService()
faculty_service = FacultyService()
course_service = CourseService()


# Add records
student_service.add_student(student)
faculty_service.add_faculty(faculty)
course_service.add_course(course)


# List records
print("\nStudents:")
for s in student_service.list_students():
    s.display_details()

print("\nFaculty:")
for f in faculty_service.list_faculty():
    f.display_details()

print("\nCourses:")
for c in course_service.list_courses():
    c.display_details()


# Update student
print("\n--- UPDATE STUDENT ---")

student_service.update_student(
    "ST001",
    age=21
)

student.display_details()


# Update course
print("\n--- UPDATE COURSE ---")

course_service.update_course(
    "CS101",
    course_name="Advanced Python",
    credits=5
)

course.display_details()


# Remove faculty
# print("\n--- REMOVE FACULTY ---")

# faculty_service.remove_faculty("FC001")

# print("Faculty list:", faculty_service.list_faculty())

print("\n--- TESTING ID GENERATOR ---")

student_id_generator = id_generator("ST")
faculty_id_generator = id_generator("FC")
course_id_generator = id_generator("CS")

print("Student IDs:")
print(student_id_generator())
print(student_id_generator())
print(student_id_generator())

print("\nFaculty IDs:")
print(faculty_id_generator())
print(faculty_id_generator())

print("\nCourse IDs:")
print(course_id_generator())
print(course_id_generator())

print("\n--- FUNCTIONAL PROGRAMMING ---")

# Get all students
students = student_service.list_students()


# MAP - Display names in uppercase
print("\nStudent Names in Uppercase:")

uppercase_names = map(
    lambda student: student.name.upper(),
    students
)

for name in uppercase_names:
    print(name)


# FILTER - Students from a particular department
print("\nStudents from Computer Science:")

cs_students = filter(
    lambda student: student.department == "Computer Science",
    students
)

for student in cs_students:
    print(student.name)


# SORTED - Sort students by name
print("\nStudents Sorted by Name:")

sorted_students = sorted(
    students,
    key=lambda student: student.name
)

for student in sorted_students:
    print(student.name)

print("\n--- WEEK 3: GENERATOR TESTING ---")

print("\nStudent Report:")

for student in student_report(student_service.list_students()):
    student.display_details()


print("\nFaculty Report:")

for faculty in faculty_service.list_faculty():
    for member in faculty_report([faculty]):
        member.display_details()


print("\nCourse Report:")

for course in course_report(course_service.list_courses()):
    course.display_details()

from app.utils.file_manager import ReportWriter

print("\n--- REPORT WRITER TESTING ---")

with ReportWriter("reports/student.txt") as file:

    for student in student_report(student_service.list_students()):
        file.write(
            f"Student ID: {student.student_id}\n"
            f"Name: {student.name}\n"
            f"Age: {student.age}\n"
            f"Email: {student.email}\n"
            f"Department: {student.department}\n\n"
        )

print("Student report created successfully.")

# Faculty Report

with ReportWriter("reports/faculty.txt") as file:

    for faculty in faculty_report(faculty_service.list_faculty()):
        file.write(
            f"Faculty ID: {faculty.faculty_id}\n"
            f"Name: {faculty.name}\n"
            f"Age: {faculty.age}\n"
            f"Email: {faculty.email}\n"
            f"Department: {faculty.department}\n\n"
        )

print("Faculty report created successfully.")


# Course Report

with ReportWriter("reports/courses.txt") as file:

    for course in course_report(course_service.list_courses()):
        file.write(
            f"Course Code: {course.course_code}\n"
            f"Course Name: {course.course_name}\n"
            f"Credits: {course.credits}\n\n"
        )

print("Course report created successfully.")

print("\n--- STUDENT ITERATOR TESTING ---")

students = student_service.list_students()

student_iterator = StudentIterator(students)

for student in student_iterator:
    print(
        f"{student.student_id} - "
        f"{student.name} - "
        f"{student.department}"
    )

print("\n--- WEEK 4: THREADING TEST ---")

generate_reports_concurrently(
    student_service.list_students(),
    faculty_service.list_faculty(),
    course_service.list_courses()
)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()

    compare_execution()

    print("\n--- WEEK 5: ASYNCIO TEST ---")

    asyncio.run(run_async_reports())

    print("\n--- ASYNC API TEST ---")

    api_results = asyncio.run(fetch_multiple_apis())

    for result in api_results:
        print(result)

    print("\n--- WEEK 5: ASYNC DATA LOADING ---")

    asyncio.run(load_all_data())

    asyncio.run(generate_all_reports())

    print("\n--- WEEK 6: JSON SERIALIZATION TEST ---")

    save_student_json([student])
    save_courses_json([course])

    print("\nLoaded Student Data:")
    print(load_student_json())

    print("\nLoaded Course Data:")
    print(load_courses_json())

    print("\n--- WEEK 6: REGEX VALIDATION TEST ---")

    try:
        validate_email("raj@gmail.com")
        print("Valid Email: raj@gmail.com")
    except ValueError as e:
        print("Error:", e)

    try:
        validate_email("rajgmail.com")
        print("Valid Email: rajgmail.com")
    except ValueError as e:
        print("Error:", e)

    try:
        validate_student_id("ST001")
        print("Valid Student ID: ST001")
    except ValueError as e:
        print("Error:", e)

    try:
        validate_student_id("ABC001")
        print("Valid Student ID: ABC001")
    except ValueError as e:
        print("Error:", e)

    print("\n--- WEEK 6: CSV TEST ---")

    export_students_csv([student])

    print("\nImported Student Data:")
    print(import_students_csv())

    print("\n--- WEEK 6: PICKLE TEST ---")

    save_students_pickle([student])

    print("\nLoaded Student Objects:")

    loaded_students = load_students_pickle()

    for s in loaded_students:
        print(
            s.student_id,
            "-",
            s.name,
            "-",
            s.department
        )

        print("\n--- WEEK 6: DYNAMIC MODULE TEST ---")

        module = load_module("math")

        if module:
            print("5 squared:", module.pow(5, 2))

    # print("\n--- WEEK 7: DATABASE TEST ---")

    # student = StudentDB(
    #     student_id="DB001",
    #     name="Test Student",
    #     age=21,
    #     email="test@gmail.com",
    #     department="Computer Science"
    # )

    # session.add(student)
    # session.commit()

    # students = session.query(StudentDB).all()

    # print("Students stored in SQLite:")

    # for s in students:
    #     print(
    #         s.student_id,
    #         "-",
    #         s.name,
    #         "-",
    #         s.department
    #     )

    # session.close()