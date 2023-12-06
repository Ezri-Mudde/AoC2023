from typing import Dict, List

from joblib import Parallel, delayed

seed_ranges: List[tuple[int, int]] = []

maps: Dict[str, List[Dict[str, int]]] = {}

with open("day5/input", "r") as f:
    filling = ""
    for line in f.readlines():
        line = line.strip()
        if line.startswith("seeds: "):
            line = line.split(": ")[-1]
            numbers = [int(seed) for seed in line.split(" ")]
            for i in range(0, len(numbers), 2):
                seed_ranges.append((numbers[i], numbers[i + 1]))
            continue
        elif line.endswith(" map:"):
            filling = line.split(" ")[0]
            if filling not in maps:
                maps[filling] = []
            continue
        elif line == "":
            filling = ""
            continue
        if filling == "":
            continue
        destination_start, source_start, range_length = (
            int(number) for number in line.split(" ")
        )

        maps[filling].append(
            {
                "source_start": source_start,
                "destination_start": destination_start,
                "range_length": range_length,
            }
        )


def get_corresponding_from_mapping(mapping_name: str, number: int) -> int:
    result = None
    for mapping_range in maps[mapping_name]:
        if (
            number >= mapping_range["source_start"]
            and number <= mapping_range["source_start"] + mapping_range["range_length"]
        ):
            result = mapping_range["destination_start"] + (
                number - mapping_range["source_start"]
            )
            break
    if result is None:
        return number
    return result


product_types = [
    "seed",
    "soil",
    "fertilizer",
    "water",
    "light",
    "temperature",
    "humidity",
    "location",
]


def min_location_for_seed_range(seed_range: tuple[int, int]) -> int:
    result = None
    for seed in range(seed_range[0], seed_range[0] + seed_range[1]):
        value = seed
        for i in range(len(product_types)):
            if i + 1 == len(product_types):
                break
            source_type = product_types[i]
            destination_type = product_types[i + 1]
            value = get_corresponding_from_mapping(
                f"{source_type}-to-{destination_type}", value
            )
        if result is None:
            result = value
        else:
            result = min(result, value)
    print(f"Result for range {seed_range} is {result}")
    return result


# Takes a looooooooong time to run
locations = Parallel(n_jobs=8)(
    delayed(min_location_for_seed_range)(seed_range) for seed_range in seed_ranges
)

print(locations)

print(min(locations))
