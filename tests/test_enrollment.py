from app.services.enrollment_service import EnrollmentService
from app.services.student_service import StudentService
from app.services.course_service import CourseService
from app.models.student import Student
from app.models.course import Course


TEST_STUDENT_ID = "ST998"
TEST_COURSE_CODE = "CS998"


def cleanup_data():
    enrollment_service = EnrollmentService()

    enrollments = enrollment_service.list_enrollments()

    for enrollment in enrollments:
        if (
            enrollment.student_id == TEST_STUDENT_ID
            and enrollment.course_code == TEST_COURSE_CODE
        ):
            enrollment_service.remove_enrollment(
                enrollment.enrollment_id
            )

    student_service = StudentService()

    students = student_service.list_students()

    for student in students:
        if student.student_id == TEST_STUDENT_ID:
            student_service.remove_student(TEST_STUDENT_ID)

    course_service = CourseService()

    courses = course_service.list_courses()

    for course in courses:
        if course.course_code == TEST_COURSE_CODE:
            course_service.remove_course(TEST_COURSE_CODE)


def create_test_data():
    student_service = StudentService()

    student = Student(
        TEST_STUDENT_ID,
        "Enrollment Test Student",
        21,
        "enrollmenttest@gmail.com",
        "Computer Science"
    )

    student_service.add_student(student)

    course_service = CourseService()

    course = Course(
        TEST_COURSE_CODE,
        "Enrollment Test Course",
        3
    )

    course_service.add_course(course)


def test_add_enrollment():
    cleanup_data()
    create_test_data()

    service = EnrollmentService()

    enrollment = service.add_enrollment(
        TEST_STUDENT_ID,
        TEST_COURSE_CODE
    )

    assert enrollment.student_id == TEST_STUDENT_ID
    assert enrollment.course_code == TEST_COURSE_CODE

    service.remove_enrollment(enrollment.enrollment_id)

    cleanup_data()


def test_search_enrollment():
    cleanup_data()
    create_test_data()

    service = EnrollmentService()

    enrollment = service.add_enrollment(
        TEST_STUDENT_ID,
        TEST_COURSE_CODE
    )

    enrollments = service.list_enrollments()

    found_enrollment = next(
        item
        for item in enrollments
        if item.enrollment_id == enrollment.enrollment_id
    )

    assert found_enrollment.student_id == TEST_STUDENT_ID
    assert found_enrollment.course_code == TEST_COURSE_CODE

    service.remove_enrollment(enrollment.enrollment_id)

    cleanup_data()


def test_delete_enrollment():
    cleanup_data()
    create_test_data()

    service = EnrollmentService()

    enrollment = service.add_enrollment(
        TEST_STUDENT_ID,
        TEST_COURSE_CODE
    )

    enrollment_id = enrollment.enrollment_id

    service.remove_enrollment(enrollment_id)

    enrollments = service.list_enrollments()

    assert not any(
        item.enrollment_id == enrollment_id
        for item in enrollments
    )

    cleanup_data()


def test_enrollment_list():
    cleanup_data()
    create_test_data()

    service = EnrollmentService()

    enrollment = service.add_enrollment(
        TEST_STUDENT_ID,
        TEST_COURSE_CODE
    )

    enrollments = service.list_enrollments()

    assert len(enrollments) > 0

    assert any(
        item.student_id == TEST_STUDENT_ID
        and item.course_code == TEST_COURSE_CODE
        for item in enrollments
    )

    service.remove_enrollment(enrollment.enrollment_id)

    cleanup_data()