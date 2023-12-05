import re
from typing import List


def check_symbol_list(
    symbol_index_line: List[int], start_pos: int, end_pos: int
) -> bool:
    for symbol_index in symbol_index_line:
        if symbol_index >= (start_pos - 1) and symbol_index <= (end_pos + 1):
            return True
    return False


symbols_regex = re.compile(r"[\#\$\%\&\*\+\-\/\=\@]")

symbol_indexes: List[List[int]] = []
lines: List[str] = []

with open("day3/input", "r") as f:
    line_count = 0
    for line in f.readlines():
        line_count += 1
        line_symbol_indexes: List[int] = []
        start_index = 0
        while match := symbols_regex.search(line, pos=start_index):
            start_index = match.end()
            line_symbol_indexes.append(match.start())
        symbol_indexes.append(line_symbol_indexes)
        lines.append(line)

print(f"line count {line_count}")

number_regex = re.compile(r"([0-9]+)")

total = 0
line_count = 0
for line_index in range(len(lines)):
    line_count += 1
    line = lines[line_index]
    start_index = 0
    while match := number_regex.search(line, pos=start_index):
        start_index = match.end()
        if (
            (  # Check line above for symbols
                line_index != 0
                and check_symbol_list(
                    symbol_indexes[line_index - 1], match.start(), match.end()
                )
            )
            or (  # Check current line for symbols
                check_symbol_list(
                    symbol_indexes[line_index], match.start(), match.end()
                )
            )
            or (  # Check line below for symbols
                line_index != len(lines) - 1
                and check_symbol_list(
                    symbol_indexes[line_index + 1], match.start(), match.end()
                )
            )
        ):
            total += int(line[match.start() : match.end()])
            continue

print(total)
