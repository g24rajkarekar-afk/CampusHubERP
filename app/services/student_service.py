from app.utils.decorators import log_decorator, time_decorator
from app.utils.logger import log_info, log_error
from app.database.db import SessionLocal
from app.database.repository import StudentRepository
from app.database.models import StudentDB
from app.models.student import Student


class StudentService:

    def __init__(self):
        self.session = SessionLocal()
        self.repository = StudentRepository(self.session)

    @log_decorator
    @time_decorator
    def add_student(self, student):

        try:
            student_db = StudentDB(
                student_id=student.student_id,
                name=student.name,
                age=student.age,
                email=student.email,
                department=student.department
            )

            self.repository.add_student(student_db)

            log_info(f"Student Added: {student.student_id}")
            print("Student added successfully.")

        except Exception as e:
            log_error(
                f"Error adding Student {student.student_id}: {e}"
            )
            raise

    @log_decorator
    @time_decorator
    def remove_student(self, student_id):

        try:
            student = self.repository.delete_student(student_id)

            if student:
                log_info(
                    f"Student Deleted: {student_id}"
                )

                print("Student removed successfully.")

            else:
                log_error(
                    f"Student not found: {student_id}"
                )

                print("Student not found.")

        except Exception as e:
            log_error(
                f"Error deleting Student {student_id}: {e}"
            )
            raise

    @log_decorator
    @time_decorator
    def update_student(
        self,
        student_id,
        name=None,
        age=None,
        email=None,
        department=None
    ):

        try:
            data = {}

            if name is not None:
                data["name"] = name

            if age is not None:
                data["age"] = age

            if email is not None:
                data["email"] = email

            if department is not None:
                data["department"] = department

            student = self.repository.update_student(
                student_id,
                data
            )

            if student:
                log_info(
                    f"Student Updated: {student_id}"
                )

                print("Student updated successfully.")

            else:
                log_error(
                    f"Student not found: {student_id}"
                )

                print("Student not found.")

        except Exception as e:
            log_error(
                f"Error updating Student {student_id}: {e}"
            )
            raise

    @log_decorator
    @time_decorator
    def list_students(self):

        try:
            students_db = self.repository.get_students()

            students = []

            for student_db in students_db:

                student = Student(
                    student_db.student_id,
                    student_db.name,
                    student_db.age,
                    student_db.email,
                    student_db.department
                )

                students.append(student)

            return students

        except Exception as e:
            log_error(
                f"Error listing students: {e}"
            )
            raise