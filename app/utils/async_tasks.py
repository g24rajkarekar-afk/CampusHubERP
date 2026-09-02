import asyncio
import time


async def generate_report(report_name):
    print(f"Starting {report_name}...")

    await asyncio.sleep(2)

    print(f"{report_name} completed.")

    return f"{report_name} completed"


async def run_async_reports():
    start_time = time.time()

    results = await asyncio.gather(
        generate_report("Student Report"),
        generate_report("Faculty Report"),
        generate_report("Course Report")
    )

    end_time = time.time()

    execution_time = end_time - start_time

    print("\nAsync Results:")

    for result in results:
        print(result)

    print(
        f"\nAsync Execution Time: "
        f"{execution_time:.2f} seconds"
    )