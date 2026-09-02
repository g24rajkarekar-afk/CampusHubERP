from app.database.models import (
    StudentDB,
    FacultyDB,
    CourseDB,
    EnrollmentDB
)

class StudentRepository:

    def __init__(self, session):
        self.session = session

    def add_student(self, student):

        existing_student = self.session.query(StudentDB).filter_by(
            student_id=student.student_id
        ).first()

        if existing_student:
            raise ValueError(
                f"Duplicate Student ID: {student.student_id}"
            )

        self.session.add(student)
        self.session.commit()

        return student

    def get_students(self):
        return self.session.query(StudentDB).all()

    def update_student(self, student_id, data):

        student = self.session.query(StudentDB).filter_by(
            student_id=student_id
        ).first()

        if student:
            for key, value in data.items():
                setattr(student, key, value)

            self.session.commit()

        return student

    def delete_student(self, student_id):

        student = self.session.query(StudentDB).filter_by(
            student_id=student_id
        ).first()

        if student:
            self.session.delete(student)
            self.session.commit()

        return student

class FacultyRepository:

    def __init__(self, session):
        self.session = session

    def add_faculty(self, faculty):

        existing_faculty = self.session.query(FacultyDB).filter_by(
            faculty_id=faculty.faculty_id
        ).first()

        if existing_faculty:
            print("Faculty already exists.")
            return existing_faculty

        self.session.add(faculty)
        self.session.commit()

        return faculty

    def get_faculty(self):
        return self.session.query(FacultyDB).all()

    def update_faculty(self, faculty_id, data):

        faculty = self.session.query(FacultyDB).filter_by(
            faculty_id=faculty_id
        ).first()

        if faculty:
            for key, value in data.items():
                setattr(faculty, key, value)

            self.session.commit()

        return faculty

    def delete_faculty(self, faculty_id):

        faculty = self.session.query(FacultyDB).filter_by(
            faculty_id=faculty_id
        ).first()

        if faculty:
            self.session.delete(faculty)
            self.session.commit()

        return faculty

class CourseRepository:

    def __init__(self, session):
        self.session = session

    def add_course(self, course):

        existing_course = self.session.query(CourseDB).filter_by(
            course_code=course.course_code
        ).first()

        if existing_course:
            print("Course already exists.")
            return existing_course

        self.session.add(course)
        self.session.commit()

        return course

    def get_courses(self):
        return self.session.query(CourseDB).all()

    def update_course(self, course_code, data):

        course = self.session.query(CourseDB).filter_by(
            course_code=course_code
        ).first()

        if course:
            for key, value in data.items():
                setattr(course, key, value)

            self.session.commit()

        return course

    def delete_course(self, course_code):

        course = self.session.query(CourseDB).filter_by(
            course_code=course_code
        ).first()

        if course:
            self.session.delete(course)
            self.session.commit()

        return course

class EnrollmentRepository:

    def __init__(self, session):
        self.session = session

    def add_enrollment(self, enrollment):

        # Check whether student exists
        student = self.session.query(StudentDB).filter_by(
            student_id=enrollment.student_id
        ).first()

        if not student:
            raise ValueError(
                f"Student not found: {enrollment.student_id}"
            )

        course = self.session.query(CourseDB).filter_by(
            course_code=enrollment.course_code
        ).first()

        if not course:
            raise ValueError(
                f"Course not found: {enrollment.course_code}"
            )

        self.session.add(enrollment)
        self.session.commit()
        self.session.refresh(enrollment)

        return enrollment

    def get_enrollments(self):
        return self.session.query(EnrollmentDB).all()

    def delete_enrollment(self, enrollment_id):

        enrollment = self.session.query(EnrollmentDB).filter_by(
            enrollment_id=enrollment_id
        ).first()

        if enrollment:
            self.session.delete(enrollment)
            self.session.commit()

        return enrollment