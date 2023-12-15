from typing import List


def parse_input(file_name: str) -> tuple[tuple[int, int], List[List[str]]]:
    starting_point: tuple[int, int] = (0, 0)
    diagram: List[List[str]] = []

    with open(file_name, "r") as f:
        lines = f.readlines()
        for index in range(len(lines)):
            row = [char for char in lines[index].strip()]
            diagram.append(row)
            if "S" in row:
                starting_point = (index, row.index("S"))

    return starting_point, diagram


def determine_starting_type(
    starting_point: tuple[int, int], diagram: List[List[str]]
) -> str:
    # ["|", "-", "L", "J", "7", "F"]:
    if (
        diagram[starting_point[0] - 1][starting_point[1]] in ["|", "7", "F"]  # North
    ) and (
        diagram[starting_point[0] + 1][starting_point[1]] in ["|", "L", "J"]  # South
    ):
        return "|"

    if (
        diagram[starting_point[0]][starting_point[1] - 1] in ["-", "L", "F"]  # West
    ) and (
        diagram[starting_point[0]][starting_point[1] + 1] in ["-", "J", "7"]  # East
    ):
        return "-"

    if (
        diagram[starting_point[0] - 1][starting_point[1]] in ["|", "7", "F"]  # North
    ) and (
        diagram[starting_point[0]][starting_point[1] + 1] in ["-", "J", "7"]  # East
    ):
        return "L"

    if (
        diagram[starting_point[0] - 1][starting_point[1]] in ["|", "7", "F"]  # North
    ) and (
        diagram[starting_point[0]][starting_point[1] - 1] in ["-", "L", "F"]  # West
    ):
        return "J"

    if (
        diagram[starting_point[0] + 1][starting_point[1]] in ["|", "L", "J"]  # South
    ) and (
        diagram[starting_point[0]][starting_point[1] - 1] in ["-", "L", "F"]  # West
    ):
        return "7"

    if (
        diagram[starting_point[0] + 1][starting_point[1]] in ["|", "L", "J"]  # South
    ) and (
        diagram[starting_point[0]][starting_point[1] + 1] in ["-", "J", "7"]  # East
    ):
        return "F"

    raise ValueError("None of the options are possible")


def determine_next_point(
    previous_point: tuple[int, int],
    current_point_type: str,
    current_point: tuple[int, int],
) -> tuple[int, int]:
    next_point: tuple[int, int] = (0, 0)
    match current_point_type:
        case "|":
            next_point = (current_point[0] - 1, current_point[1])  # North
            if next_point == previous_point:
                next_point = (current_point[0] + 1, current_point[1])  # South
            elif next_point[0] < 0 or next_point[1] < 0:
                next_point = (current_point[0] + 1, current_point[1])  # South
        case "-":
            next_point = (current_point[0], current_point[1] + 1)  # East
            if next_point == previous_point:
                next_point = (current_point[0], current_point[1] - 1)  # West
            elif next_point[0] < 0 or next_point[1] < 0:
                next_point = (current_point[0], current_point[1] - 1)  # West
        case "L":
            next_point = (current_point[0] - 1, current_point[1])  # North
            if next_point == previous_point:
                next_point = (current_point[0], current_point[1] + 1)  # East
            elif next_point[0] < 0 or next_point[1] < 0:
                next_point = (current_point[0], current_point[1] + 1)  # East
        case "J":
            next_point = (current_point[0] - 1, current_point[1])  # North
            if next_point == previous_point:
                next_point = (current_point[0], current_point[1] - 1)  # West
            elif next_point[0] < 0 or next_point[1] < 0:
                next_point = (current_point[0], current_point[1] - 1)  # West
        case "7":
            next_point = (current_point[0] + 1, current_point[1])  # South
            if next_point == previous_point:
                next_point = (current_point[0], current_point[1] - 1)  # West
            elif next_point[0] < 0 or next_point[1] < 0:
                next_point = (current_point[0], current_point[1] - 1)  # West
        case "F":
            next_point = (current_point[0] + 1, current_point[1])  # South

            if next_point == previous_point:
                next_point = (current_point[0], current_point[1] + 1)  # East
            elif next_point[0] < 0 or next_point[1] < 0:
                next_point = (current_point[0], current_point[1] + 1)  # East
        case _:
            raise ValueError("None of the options are possible")
    return next_point


def calculate_farthest_point(file_name: str) -> None:
    print(f"For file {file_name}")
    starting_point, diagram = parse_input(file_name)
    print(f"Starting point is {starting_point}")

    starting_point_type = determine_starting_type(
        starting_point=starting_point, diagram=diagram
    )
    print(f"Starting point is of type {starting_point_type}")
    diagram[starting_point[0]][starting_point[1]] = starting_point_type

    previous_point = starting_point
    current_point = determine_next_point(
        previous_point=previous_point,
        current_point_type=starting_point_type,
        current_point=starting_point,
    )

    steps = 1

    while current_point != starting_point:
        previous_point, current_point = current_point, determine_next_point(
            previous_point=previous_point,
            current_point_type=diagram[current_point[0]][current_point[1]],
            current_point=current_point,
        )

        steps += 1
    print(f"Total steps to do loop is {steps} farthest point is at {steps/2}")


if __name__ == "__main__":
    calculate_farthest_point("day10/test_input")
    calculate_farthest_point("day10/input")
