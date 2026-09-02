from app.models.faculty import Faculty
from app.services.faculty_service import FacultyService


TEST_ID = "FC999"


def cleanup_faculty():
    service = FacultyService()

    faculties = service.list_faculty()

    for faculty in faculties:
        if faculty.faculty_id == TEST_ID:
            service.remove_faculty(TEST_ID)


def test_add_faculty():
    cleanup_faculty()

    service = FacultyService()

    faculty = Faculty(
        TEST_ID,
        "Test Faculty",
        35,
        "testfaculty@gmail.com",
        "Computer Science"
    )

    service.add_faculty(faculty)

    faculties = service.list_faculty()

    assert any(
        faculty.faculty_id == TEST_ID
        for faculty in faculties
    )

    cleanup_faculty()


def test_update_faculty():
    cleanup_faculty()

    service = FacultyService()

    faculty = Faculty(
        TEST_ID,
        "Test Faculty",
        35,
        "testfaculty@gmail.com",
        "Computer Science"
    )

    service.add_faculty(faculty)

    service.update_faculty(
        TEST_ID,
        "Updated Faculty",
        36,
        "updatedfaculty@gmail.com",
        "Computer Science"
    )

    faculties = service.list_faculty()

    found_faculty = next(
        faculty for faculty in faculties
        if faculty.faculty_id == TEST_ID
    )

    assert found_faculty.name == "Updated Faculty"
    assert found_faculty.age == 36
    assert found_faculty.email == "updatedfaculty@gmail.com"
    assert found_faculty.department == "Computer Science"

    cleanup_faculty()


def test_delete_faculty():
    cleanup_faculty()

    service = FacultyService()

    faculty = Faculty(
        TEST_ID,
        "Test Faculty",
        35,
        "testfaculty@gmail.com",
        "Computer Science"
    )

    service.add_faculty(faculty)

    service.remove_faculty(TEST_ID)

    faculties = service.list_faculty()

    assert not any(
        faculty.faculty_id == TEST_ID
        for faculty in faculties
    )


def test_search_faculty():
    cleanup_faculty()

    service = FacultyService()

    faculty = Faculty(
        TEST_ID,
        "Test Faculty",
        35,
        "testfaculty@gmail.com",
        "Computer Science"
    )

    service.add_faculty(faculty)

    faculties = service.list_faculty()

    found_faculty = next(
        faculty for faculty in faculties
        if faculty.faculty_id == TEST_ID
    )

    assert found_faculty.faculty_id == TEST_ID
    assert found_faculty.name == "Test Faculty"

    cleanup_faculty()