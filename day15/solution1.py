from typing import List


def parse_input(file_name: str) -> List[str]:
    steps: List[str] = []

    with open(file_name, "r") as f:
        for line in f.readlines():
            for step in line.strip().split(","):
                steps.append(step)

    return steps


def calculate_hash(step: str) -> int:
    result = 0

    for char in step:
        result += ord(char)
        result = result * 17
        result = result % 256

    return result


def calculate_sum(file_name: str) -> None:
    print(f"Calculating sum for file {file_name}")
    steps = parse_input(file_name)

    total = 0
    for step in steps:
        step_hash = calculate_hash(step)
        print(f"The hash for step [{step}] is {step_hash}")
        total += step_hash

    print(f"The sum of all step for file {file_name} is {total}")


if __name__ == "__main__":
    calculate_sum("day15/test_input")
    calculate_sum("day15/input")
