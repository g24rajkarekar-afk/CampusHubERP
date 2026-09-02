import json
from pathlib import Path


DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)


def save_student_json(students):
    file_path = DATA_DIR / "student.json"

    data = [student.to_dict() for student in students]

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    print("Student data saved successfully.")


def load_student_json():
    file_path = DATA_DIR / "student.json"

    if not file_path.exists():
        return []

    with open(file_path, "r") as file:
        return json.load(file)


def save_courses_json(courses):
    file_path = DATA_DIR / "courses.json"

    data = [course.to_dict() for course in courses]

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    print("Course data saved successfully.")


def load_courses_json():
    file_path = DATA_DIR / "courses.json"

    if not file_path.exists():
        return []

    with open(file_path, "r") as file:
        return json.load(file)