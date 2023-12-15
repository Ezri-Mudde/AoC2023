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

    boxes: dict[int, List[tuple[str, int]]] = {box: [] for box in range(256)}

    for step in steps:
        if "=" in step:
            step_label, focal_length = step.split("=")
            step_hash = calculate_hash(step_label)
            step_lens_index = None
            for lens_index in range(len(boxes[step_hash])):
                if boxes[step_hash][lens_index][0] == step_label:
                    step_lens_index = lens_index
                    break
            if step_lens_index is None:
                boxes[step_hash].append(("", 0))
                step_lens_index = len(boxes[step_hash]) - 1
            boxes[step_hash][step_lens_index] = (step_label, int(focal_length))

        else:
            step_label = step.split("-")[0]
            step_hash = calculate_hash(step_label)
            for lens_index in range(len(boxes[step_hash])):
                if boxes[step_hash][lens_index][0] == step_label:
                    boxes[step_hash].pop(lens_index)
                    break

    total = 0
    for box, lenses in boxes.items():
        for slot in range(len(lenses)):
            focus_power = (1 + box) * (1 + slot) * lenses[slot][1]
            print(
                f"The focus power of lens {lenses[slot][0]} in slot {1+slot} in box {box} is {focus_power}"
            )
            total += focus_power

    print(f"The total focussing power for file {file_name} is {total}")


if __name__ == "__main__":
    calculate_sum("day15/test_input")
    calculate_sum("day15/input")
