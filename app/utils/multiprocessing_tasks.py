from concurrent.futures import ProcessPoolExecutor
import time


def cpu_task(number):
    total = 0

    for i in range(number):
        total += i * i

    return total


def run_sequential():
    numbers = [
        2_000_000,
        2_000_000,
        2_000_000
    ]

    start_time = time.time()

    results = []

    for number in numbers:
        results.append(cpu_task(number))

    end_time = time.time()

    execution_time = end_time - start_time

    print("\nSequential Results:")
    print(results)

    print(
        f"Sequential Time: "
        f"{execution_time:.4f} seconds"
    )

    return execution_time


def run_cpu_tasks():
    numbers = [
        2_000_000,
        2_000_000,
        2_000_000
    ]

    start_time = time.time()

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(cpu_task, numbers))

    end_time = time.time()

    execution_time = end_time - start_time

    print("\nMultiprocessing Results:")
    print(results)

    print(
        f"Multiprocessing Time: "
        f"{execution_time:.4f} seconds"
    )

    return execution_time


def compare_execution():
    print("\n--- EXECUTION TIME COMPARISON ---")

    sequential_time = run_sequential()
    multiprocessing_time = run_cpu_tasks()

    print("\nComparison:")

    if multiprocessing_time < sequential_time:
        print("Multiprocessing was faster.")
    elif sequential_time < multiprocessing_time:
        print("Sequential execution was faster.")
    else:
        print("Both took approximately the same time.")