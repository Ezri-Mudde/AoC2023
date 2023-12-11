from typing import List


def get_next_value(numbers: List[int]) -> int:
    delta: List[int] = []
    for i in range(len(numbers) - 1):
        delta.append(numbers[i + 1] - numbers[i])
    if not [num for num in delta if num != 0]:
        next_value = numbers[-1] + 0
    else:
        next_value = numbers[-1] + get_next_value(delta)

    return next_value


def get_sum_next_values(file_name: str) -> int:
    next_values: List[int] = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            values = [int(number) for number in line.split(" ")]
            next_value = get_next_value(values)
            next_values.append(next_value)
    return sum(next_values)


if __name__ == "__main__":
    test_result = get_sum_next_values("day9/test_input")
    print(f"Test result is {test_result}")
    result = get_sum_next_values("day9/input")
    print(f"Result is {result}")
