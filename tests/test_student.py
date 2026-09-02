from app.models.student import Student
from app.services.student_service import StudentService


TEST_ID = "ST999"


def cleanup_student():
    service = StudentService()

    students = service.list_students()

    for student in students:
        if student.student_id == TEST_ID:
            service.remove_student(TEST_ID)


def test_add_student():
    cleanup_student()

    service = StudentService()

    student = Student(
        TEST_ID,
        "Test Student",
        21,
        "teststudent@gmail.com",
        "Computer Science"
    )

    service.add_student(student)

    students = service.list_students()

    assert any(
        student.student_id == TEST_ID
        for student in students
    )

    cleanup_student()


def test_update_student():
    cleanup_student()

    service = StudentService()

    student = Student(
        TEST_ID,
        "Test Student",
        21,
        "teststudent@gmail.com",
        "Computer Science"
    )

    service.add_student(student)

    # IMPORTANT:
    # StudentService.update_student() expects
    # student_id, name, age, email, department separately.

    service.update_student(
        TEST_ID,
        "Updated Student",
        22,
        "updatedstudent@gmail.com",
        "Computer Science"
    )

    students = service.list_students()

    found_student = next(
        student for student in students
        if student.student_id == TEST_ID
    )

    assert found_student.name == "Updated Student"
    assert found_student.age == 22
    assert found_student.email == "updatedstudent@gmail.com"
    assert found_student.department == "Computer Science"

    cleanup_student()


def test_delete_student():
    cleanup_student()

    service = StudentService()

    student = Student(
        TEST_ID,
        "Test Student",
        21,
        "teststudent@gmail.com",
        "Computer Science"
    )

    service.add_student(student)

    service.remove_student(TEST_ID)

    students = service.list_students()

    assert not any(
        student.student_id == TEST_ID
        for student in students
    )


def test_search_student():
    cleanup_student()

    service = StudentService()

    student = Student(
        TEST_ID,
        "Test Student",
        21,
        "teststudent@gmail.com",
        "Computer Science"
    )

    service.add_student(student)

    students = service.list_students()

    found_student = next(
        student for student in students
        if student.student_id == TEST_ID
    )

    assert found_student.student_id == TEST_ID
    assert found_student.name == "Test Student"

    cleanup_student()