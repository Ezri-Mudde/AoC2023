from typing import List

empty_rows: List[int] = []
empty_columns: List[int] = []


def parse_input(file_name: str) -> List[tuple[int, int]]:
    global empty_rows, empty_columns
    galaxies: List[tuple[int, int]] = []
    empty_rows = []
    empty_columns = []

    with open(file_name, "r") as f:
        lines: List[str] = f.readlines()

    for x in range(len(lines)):
        row_empty = True
        for y in range(len(lines[x]) - 1):
            if lines[x][y] == "#":
                galaxies.append((x, y))
                row_empty = False
        if row_empty:
            empty_rows.append(x)

    for y in range(len(lines[0]) - 1):
        column_empty = True
        for line in lines:
            try:
                if line[y] == "#":
                    column_empty = False
                    break
            except IndexError:
                print("hurdurdur")
        if column_empty:
            empty_columns.append(y)

    return galaxies


def calculate_distance(
    first_galaxy: tuple[int, int], second_galaxy: tuple[int, int], factor: int = 2
) -> int:
    global empty_rows, empty_columns
    steps = 0

    for x in range(
        min(first_galaxy[0], second_galaxy[0]), max(first_galaxy[0], second_galaxy[0])
    ):
        if x in empty_rows:
            steps += factor
        else:
            steps += 1

    for y in range(
        min(first_galaxy[1], second_galaxy[1]), max(first_galaxy[1], second_galaxy[1])
    ):
        if y in empty_columns:
            steps += factor
        else:
            steps += 1

    return steps


def sum_shortest_paths(file_name: str, factor: int = 2) -> int:
    galaxies = parse_input(file_name=file_name)
    print(f"For file {file_name}")
    # print(f"Galaxies: {galaxies}")
    # print(f"Empty rows: {empty_rows}")
    # print(f"Empty columns: {empty_columns}")

    total = 0
    for index in range(len(galaxies)):
        first_galaxy = galaxies[index]
        for second_galaxy in galaxies[0:index]:
            total += calculate_distance(
                first_galaxy=first_galaxy, second_galaxy=second_galaxy, factor=factor
            )
    print(f"Sum distances with factor {factor} is: {total}")
    print()


if __name__ == "__main__":
    # Part 1
    sum_shortest_paths("day11/test_input", factor=2)
    sum_shortest_paths("day11/input", factor=2)
    # Part 2
    sum_shortest_paths("day11/test_input", factor=10)
    sum_shortest_paths("day11/test_input", factor=100)
    sum_shortest_paths("day11/input", factor=1000000)
