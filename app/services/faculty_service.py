from app.utils.decorators import log_decorator, time_decorator
from app.utils.logger import log_info, log_error
from app.database.db import SessionLocal
from app.database.repository import FacultyRepository
from app.database.models import FacultyDB
from app.models.faculty import Faculty


class FacultyService:

    def __init__(self):
        self.session = SessionLocal()
        self.repository = FacultyRepository(self.session)

    @log_decorator
    @time_decorator
    def add_faculty(self, faculty):

        try:
            faculty_db = FacultyDB(
                faculty_id=faculty.faculty_id,
                name=faculty.name,
                age=faculty.age,
                email=faculty.email,
                department=faculty.department
            )

            self.repository.add_faculty(faculty_db)

            log_info(
                f"Faculty Added: {faculty.faculty_id}"
            )

            print("Faculty added successfully.")

        except Exception as e:
            log_error(
                f"Error adding Faculty {faculty.faculty_id}: {e}"
            )
            raise

    @log_decorator
    @time_decorator
    def remove_faculty(self, faculty_id):

        try:
            faculty = self.repository.delete_faculty(faculty_id)

            if faculty:
                log_info(
                    f"Faculty Deleted: {faculty_id}"
                )

                print("Faculty removed successfully.")

            else:
                log_error(
                    f"Faculty not found: {faculty_id}"
                )

                print("Faculty not found.")

        except Exception as e:
            log_error(
                f"Error deleting Faculty {faculty_id}: {e}"
            )
            raise

    @log_decorator
    @time_decorator
    def update_faculty(
        self,
        faculty_id,
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

            faculty = self.repository.update_faculty(
                faculty_id,
                data
            )

            if faculty:
                log_info(
                    f"Faculty Updated: {faculty_id}"
                )

                print("Faculty updated successfully.")

            else:
                log_error(
                    f"Faculty not found: {faculty_id}"
                )

                print("Faculty not found.")

        except Exception as e:
            log_error(
                f"Error updating Faculty {faculty_id}: {e}"
            )
            raise

    @log_decorator
    @time_decorator
    def list_faculty(self):

        try:
            faculty_db_list = self.repository.get_faculty()

            faculty_list = []

            for faculty_db in faculty_db_list:

                faculty = Faculty(
                    faculty_db.faculty_id,
                    faculty_db.name,
                    faculty_db.age,
                    faculty_db.email,
                    faculty_db.department
                )

                faculty_list.append(faculty)

            return faculty_list

        except Exception as e:
            log_error(
                f"Error listing faculty: {e}"
            )
            raise