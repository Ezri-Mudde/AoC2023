import re
from typing import List


def check_number_list(
    number_index_line: List[tuple[int, int, int]], pos: int
) -> List[int]:
    matches: List[int] = []
    for number_index_start, number_index_end, number in number_index_line:
        if pos >= (number_index_start - 1) and pos <= (number_index_end):
            matches.append(number)
    return matches


numbers_regex = re.compile(r"([0-9]+)")

numbers_indexes: List[List[tuple[int, int, int]]] = []
lines: List[str] = []

with open("day3/input", "r") as f:
    line_count = 0
    for line in f.readlines():
        line_count += 1
        line_symbol_indexes: List[tuple[int, int, int]] = []
        start_index = 0
        while match := numbers_regex.search(line, pos=start_index):
            start_index = match.end()
            line_symbol_indexes.append(
                (match.start(), match.end(), int(line[match.start() : match.end()]))
            )
        numbers_indexes.append(line_symbol_indexes)
        lines.append(line)

print(f"line count {line_count}")

gear_regex = re.compile(r"\*")

total = 0
line_count = 0
for line_index in range(len(lines)):
    line_count += 1
    line = lines[line_index]
    start_index = 0
    while match := gear_regex.search(line, pos=start_index):
        start_index = match.end()
        matches: List[int] = []
        if line_index != 0:
            matches.extend(
                check_number_list(numbers_indexes[line_index - 1], match.start())
            )
        matches.extend(check_number_list(numbers_indexes[line_index], match.start()))
        if line_index != len(lines) - 1:
            matches.extend(
                check_number_list(numbers_indexes[line_index + 1], match.start())
            )
        if len(matches) != 2:
            continue
        total += matches[0] * matches[1]


print(total)
