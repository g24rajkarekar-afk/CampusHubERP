import pickle
from pathlib import Path


DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)


def save_students_pickle(students):
    file_path = DATA_DIR / "students.pkl"

    with open(file_path, "wb") as file:
        pickle.dump(students, file)

    print("Student data saved using pickle.")


def load_students_pickle():
    file_path = DATA_DIR / "students.pkl"

    if not file_path.exists():
        return []

    with open(file_path, "rb") as file:
        return pickle.load(file)