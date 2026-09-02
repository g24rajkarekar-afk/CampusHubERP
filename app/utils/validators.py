import re


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(pattern, email):
        raise ValueError("Invalid email format")

    return True


def validate_student_id(student_id):
    pattern = r"^ST\d{3}$"

    if not re.match(pattern, student_id):
        raise ValueError("Invalid student ID format")

    return True