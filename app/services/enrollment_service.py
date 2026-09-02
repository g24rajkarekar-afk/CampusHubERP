from app.utils.decorators import log_decorator, time_decorator
from app.utils.logger import log_info, log_error
from app.database.db import SessionLocal
from app.database.repository import EnrollmentRepository
from app.database.models import EnrollmentDB


class EnrollmentService:

    def __init__(self):
        self.session = SessionLocal()
        self.repository = EnrollmentRepository(self.session)

    @log_decorator
    @time_decorator
    def add_enrollment(self, student_id, course_code):

        try:
            enrollment_db = EnrollmentDB(
                student_id=student_id,
                course_code=course_code
            )

            enrollment = self.repository.add_enrollment(
                enrollment_db
            )

            log_info(
                f"Enrollment Created: Student {student_id}, Course {course_code}"
            )

            return enrollment

        except Exception as e:
            log_error(
                f"Error creating Enrollment: Student {student_id}, "
                f"Course {course_code}: {e}"
            )
            raise

    @log_decorator
    @time_decorator
    def list_enrollments(self):

        try:
            return self.repository.get_enrollments()

        except Exception as e:
            log_error(f"Error listing Enrollments: {e}")
            raise

    @log_decorator
    @time_decorator
    def remove_enrollment(self, enrollment_id):

        try:
            enrollment = self.repository.delete_enrollment(
                enrollment_id
            )

            if enrollment:
                log_info(
                    f"Enrollment Deleted: {enrollment_id}"
                )
            else:
                log_error(
                    f"Enrollment not found: {enrollment_id}"
                )

            return enrollment

        except Exception as e:
            log_error(
                f"Error deleting Enrollment {enrollment_id}: {e}"
            )
            raise