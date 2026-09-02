from concurrent.futures import ThreadPoolExecutor

from app.utils.file_manager import ReportWriter
from app.utils.generators import (
    student_report,
    faculty_report,
    course_report
)


def write_student_report(students):
    with ReportWriter("reports/student.txt") as file:

        for student in student_report(students):
            file.write(
                f"Student ID: {student.student_id}\n"
                f"Name: {student.name}\n"
                f"Age: {student.age}\n"
                f"Email: {student.email}\n"
                f"Department: {student.department}\n\n"
            )

    return "Student report completed"


def write_faculty_report(faculty):
    with ReportWriter("reports/faculty.txt") as file:

        for member in faculty_report(faculty):
            file.write(
                f"Faculty ID: {member.faculty_id}\n"
                f"Name: {member.name}\n"
                f"Age: {member.age}\n"
                f"Email: {member.email}\n"
                f"Department: {member.department}\n\n"
            )

    return "Faculty report completed"


def write_course_report(courses):
    with ReportWriter("reports/courses.txt") as file:

        for course in course_report(courses):
            file.write(
                f"Course Code: {course.course_code}\n"
                f"Course Name: {course.course_name}\n"
                f"Credits: {course.credits}\n\n"
            )

    return "Course report completed"


def generate_reports_concurrently(
    students,
    faculty,
    courses
):
    with ThreadPoolExecutor(max_workers=3) as executor:

        tasks = [
            executor.submit(write_student_report, students),
            executor.submit(write_faculty_report, faculty),
            executor.submit(write_course_report, courses)
        ]

        for task in tasks:
            print(task.result())