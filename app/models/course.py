from datetime import datetime

from app.core.metaclasses import ModelMeta


class Course(metaclass=ModelMeta):

    def __init__(self, course_code, course_name, credits):

        if not course_code or not course_code.strip():
            raise ValueError("Course code cannot be empty")

        if not course_code.startswith("CS"):
            raise ValueError("Invalid Course Code. Course code must start with CS")

        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits

        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def display_details(self):
        print("Course Code:", self.course_code)
        print("Course Name:", self.course_name)
        print("Credits:", self.credits)

    def to_dict(self):
        return {
            "course_code": self.course_code,
            "course_name": self.course_name,
            "credits": self.credits
        }