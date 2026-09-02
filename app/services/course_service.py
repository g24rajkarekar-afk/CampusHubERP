from app.utils.decorators import log_decorator, time_decorator
from app.utils.logger import log_info, log_error
from app.database.db import SessionLocal
from app.database.repository import CourseRepository
from app.database.models import CourseDB
from app.models.course import Course


class CourseService:

    def __init__(self):
        self.session = SessionLocal()
        self.repository = CourseRepository(self.session)

    @log_decorator
    @time_decorator
    def add_course(self, course):

        try:
            course_db = CourseDB(
                course_code=course.course_code,
                course_name=course.course_name,
                credits=course.credits
            )

            self.repository.add_course(course_db)

            log_info(f"Course Added: {course.course_code}")

            print("Course added successfully.")

        except Exception as e:
            log_error(
                f"Error adding Course {course.course_code}: {e}"
            )
            raise

    @log_decorator
    @time_decorator
    def remove_course(self, course_code):

        try:
            course = self.repository.delete_course(course_code)

            if course:
                log_info(f"Course Deleted: {course_code}")
                print("Course removed successfully.")
            else:
                log_error(f"Course not found: {course_code}")
                print("Course not found.")

        except Exception as e:
            log_error(
                f"Error deleting Course {course_code}: {e}"
            )
            raise

    @log_decorator
    @time_decorator
    def update_course(
        self,
        course_code,
        course_name=None,
        credits=None
    ):

        try:
            data = {}

            if course_name is not None:
                data["course_name"] = course_name

            if credits is not None:
                data["credits"] = credits

            course = self.repository.update_course(
                course_code,
                data
            )

            if course:
                log_info(f"Course Updated: {course_code}")
                print("Course updated successfully.")
            else:
                log_error(f"Course not found: {course_code}")
                print("Course not found.")

        except Exception as e:
            log_error(
                f"Error updating Course {course_code}: {e}"
            )
            raise

    @log_decorator
    @time_decorator
    def list_courses(self):

        try:
            courses_db = self.repository.get_courses()

            courses = []

            for course_db in courses_db:

                course = Course(
                    course_db.course_code,
                    course_db.course_name,
                    course_db.credits
                )

                courses.append(course)

            return courses

        except Exception as e:
            log_error(f"Error listing courses: {e}")
            raise