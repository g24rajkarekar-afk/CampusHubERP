from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course


class ModelFactory:

    @staticmethod
    def create(model_type, **kwargs):

        if model_type.lower() == "student":
            return Student(
                kwargs["student_id"],
                kwargs["name"],
                kwargs["age"],
                kwargs["email"],
                kwargs["department"]
            )

        elif model_type.lower() == "faculty":
            return Faculty(
                kwargs["faculty_id"],
                kwargs["name"],
                kwargs["age"],
                kwargs["email"],
                kwargs["department"]
            )

        elif model_type.lower() == "course":
            return Course(
                kwargs["course_code"],
                kwargs["course_name"],
                kwargs["credits"]
            )

        else:
            raise ValueError(
                f"Unknown model type: {model_type}"
            )