from copy import copy
from typing import List


Direction = tuple[int, int, str]
Coordinate = tuple[int, int]


UP: Direction = (-1, 0, "^")
DOWN: Direction = (1, 0, "v")
LEFT: Direction = (0, -1, "<")
RIGHT: Direction = (0, 1, ">")

contraption: List[List[str]] = []
energized_tiles: List[tuple[Coordinate, Direction]] = []


def parse_input(file_name: str) -> None:
    global contraption
    with open(file_name, "r") as f:
        contraption = [[char for char in line.strip()] for line in f.readlines()]


def traverse_contraption(
    starting_point: Coordinate = (0, 0), direction: Direction = RIGHT
) -> None:
    global energized_tiles

    done = False
    current_point = starting_point
    while not done:
        next_point = (current_point[0] + direction[0], current_point[1] + direction[1])
        # Check if out of bounds
        if next_point[0] < 0 or next_point[0] >= len(contraption):
            break
        elif next_point[1] < 0 or next_point[1] >= len(contraption[0]):
            break
        elif (
            # Check if we've already been here going the same direction
            (current_point, direction) in energized_tiles
            and (next_point, direction) in energized_tiles
        ):
            break
        next_type = contraption[next_point[0]][next_point[1]]
        energized_tiles.append((next_point, direction))

        if next_type == "/":
            if direction == UP:
                direction = RIGHT
            elif direction == DOWN:
                direction = LEFT
            elif direction == LEFT:
                direction = DOWN
            elif direction == RIGHT:
                direction = UP
        elif next_type == "\\":
            if direction == UP:
                direction = LEFT
            elif direction == DOWN:
                direction = RIGHT
            elif direction == LEFT:
                direction = UP
            elif direction == RIGHT:
                direction = DOWN
        elif next_type == "-":
            if direction == UP or direction == DOWN:
                traverse_contraption(next_point, LEFT)
                traverse_contraption(next_point, RIGHT)
                done = True
        elif next_type == "|":
            if direction == LEFT or direction == RIGHT:
                traverse_contraption(next_point, UP)
                traverse_contraption(next_point, DOWN)
                done = True

        current_point = next_point


def print_traversed() -> None:
    global contraption
    global energized_tiles
    result = copy(contraption)
    for tile in energized_tiles:
        result[tile[0][0]][tile[0][1]] = "#"

    diagram = "\n".join(["".join(line) for line in result])
    print(diagram)
    print(diagram.count("#"))


def determine_count(
    starting_point: Coordinate = (0, -1), direction: Direction = RIGHT
) -> int:
    global energized_tiles
    energized_tiles = []

    traverse_contraption(starting_point=starting_point, direction=direction)
    unique_energized = set([tile[0] for tile in energized_tiles])
    return len(unique_energized)


def determine_best_point() -> tuple[int, Coordinate]:
    global contraption
    options: List[tuple[Coordinate, int]] = []

    best_score = 0
    best_point = (0, -1)

    for x in range(len(contraption)):
        one_way = ((x, -1), determine_count((x, -1), RIGHT))
        if one_way[1] > best_score:
            best_score = one_way[1]
            best_point = one_way[0]
        options.append(one_way)
        other_way = (
            (x, len(contraption[x])),
            determine_count((x, len(contraption[x])), LEFT),
        )
        if other_way[1] > best_score:
            best_score = other_way[1]
            best_point = other_way[0]
        options.append(other_way)

    for y in range(len(contraption[0])):
        one_way = ((-1, y), determine_count((-1, y), DOWN))
        if one_way[1] > best_score:
            best_score = one_way[1]
            best_point = one_way[0]
        options.append(one_way)
        other_way = ((len(contraption), y), determine_count((len(contraption), y), UP))
        if other_way[1] > best_score:
            best_score = other_way[1]
            best_point = other_way[0]
        options.append(other_way)

    return best_score, best_point


if __name__ == "__main__":
    parse_input("day16/test_input")
    print(determine_count())  # Part one
    print(determine_best_point())  # Part two
    parse_input("day16/input")
    print(determine_count())
    print(determine_best_point())
