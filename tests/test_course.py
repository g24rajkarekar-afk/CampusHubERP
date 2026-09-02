from app.models.course import Course
from app.services.course_service import CourseService


TEST_CODE = "CS999"


def cleanup_course():
    service = CourseService()

    courses = service.list_courses()

    for course in courses:
        if course.course_code == TEST_CODE:
            service.remove_course(TEST_CODE)


def test_add_course():
    cleanup_course()

    service = CourseService()

    course = Course(
        TEST_CODE,
        "Test Course",
        3
    )

    service.add_course(course)

    courses = service.list_courses()

    assert any(
        course.course_code == TEST_CODE
        for course in courses
    )

    cleanup_course()


def test_update_course():
    cleanup_course()

    service = CourseService()

    course = Course(
        TEST_CODE,
        "Test Course",
        3
    )

    service.add_course(course)

    service.update_course(
        TEST_CODE,
        "Updated Course",
        4
    )

    courses = service.list_courses()

    found_course = next(
        course for course in courses
        if course.course_code == TEST_CODE
    )

    assert found_course.course_name == "Updated Course"
    assert found_course.credits == 4

    cleanup_course()


def test_delete_course():
    cleanup_course()

    service = CourseService()

    course = Course(
        TEST_CODE,
        "Test Course",
        3
    )

    service.add_course(course)

    service.remove_course(TEST_CODE)

    courses = service.list_courses()

    assert not any(
        course.course_code == TEST_CODE
        for course in courses
    )


def test_search_course():
    cleanup_course()

    service = CourseService()

    course = Course(
        TEST_CODE,
        "Test Course",
        3
    )

    service.add_course(course)

    courses = service.list_courses()

    found_course = next(
        course for course in courses
        if course.course_code == TEST_CODE
    )

    assert found_course.course_code == TEST_CODE
    assert found_course.course_name == "Test Course"

    cleanup_course()