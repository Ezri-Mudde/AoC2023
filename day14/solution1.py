from typing import List


def parse_input(file_name: str) -> List[str]:
    dish: List[str] = []

    with open(file_name, "r") as f:
        lines = f.readlines()
        for index in range(len(lines[0].strip()) - 1, -1, -1):
            dish_line = ""
            for line in reversed(lines):
                dish_line = line[index] + dish_line
            dish.append(dish_line)

    return dish


def tilt_dish(dish: List[str]) -> List[str]:
    for line_index in range(len(dish)):
        line = dish[line_index]
        start = 0
        end = len(line)
        while start != end:
            if "#" in line[start:end]:
                rock_index = line.index("#", start)
            else:
                rock_index = end
            line = (
                line[0:start]
                + "".join(sorted(line[start:rock_index], reverse=True))
                + line[rock_index:end]
            )
            if rock_index == end:
                break
            start = rock_index + 1
        dish[line_index] = line

    return dish


def calculate_load(file_name: str):
    print(f"For input file {file_name}")
    dish = parse_input(file_name=file_name)
    print("Dish is:")
    print("\n".join(dish))
    print()
    tilted_dish = tilt_dish(dish=dish)
    print("Tilted dish is")
    print("\n".join(tilted_dish))
    print()
    total = 0

    for line in tilted_dish:
        for index in range(len(line)):
            if line[index] == "O":
                total += len(line) - index

    print(f"Total load is {total}")


if __name__ == "__main__":
    calculate_load("day14/test_input")
    calculate_load("day14/input")
