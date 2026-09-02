import asyncio


async def load_students():
    print("Loading Students...")
    await asyncio.sleep(1)
    return "Students loaded"


async def load_faculty():
    print("Loading Faculty...")
    await asyncio.sleep(1)
    return "Faculty loaded"


async def load_courses():
    print("Loading Courses...")
    await asyncio.sleep(1)
    return "Courses loaded"


async def load_enrollments():
    print("Loading Enrollments...")
    await asyncio.sleep(1)
    return "Enrollments loaded"


async def load_all_data():

    results = await asyncio.gather(
        load_students(),
        load_faculty(),
        load_courses(),
        load_enrollments()
    )

    print("All data loaded successfully.")

    return results

async def generate_student_report():
    await asyncio.sleep(1)
    print("Student Report Completed")


async def generate_faculty_report():
    await asyncio.sleep(1)
    print("Faculty Report Completed")


async def generate_course_report():
    await asyncio.sleep(1)
    print("Course Report Completed")


async def generate_all_reports():

    print("\nGenerating Reports...")

    await asyncio.gather(
        generate_student_report(),
        generate_faculty_report(),
        generate_course_report()
    )

    print("\nAll Reports Generated Successfully.")