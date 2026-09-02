import csv
from pathlib import Path


DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)


def export_students_csv(students):
    file_path = DATA_DIR / "students.csv"

    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "student_id",
            "name",
            "age",
            "email",
            "department"
        ])

        for student in students:
            writer.writerow([
                student.student_id,
                student.name,
                student.age,
                student.email,
                student.department
            ])

    print("Student CSV exported successfully.")


def import_students_csv():
    file_path = DATA_DIR / "students.csv"

    if not file_path.exists():
        return []

    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)

        students = []

        for row in reader:
            students.append(dict(row))

    return students