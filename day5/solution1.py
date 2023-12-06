from typing import Dict, List


seeds: List[int] = []

maps: Dict[str, List[Dict[str, int]]] = {}

with open("day5/input", "r") as f:
    filling = ""
    for line in f.readlines():
        line = line.strip()
        if line.startswith("seeds: "):
            line = line.split(": ")[-1]
            seeds.extend([int(seed) for seed in line.split()])
            continue
        elif line.endswith(" map:"):
            filling = line.split(" ")[0]
            print(f"Start filling {filling}")
            if filling not in maps:
                maps[filling] = []
            continue
        elif line == "":
            print(f"Done filling {filling}")
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
            mapping_range["source_start"] < number
            and number < mapping_range["source_start"] + mapping_range["range_length"]
        ):
            result = mapping_range["destination_start"] + (
                number - mapping_range["source_start"]
            )
    if result is None:
        return number
    return result


locations: List[int] = []

for seed in seeds:
    soil = get_corresponding_from_mapping("seed-to-soil", seed)
    fertilizer = get_corresponding_from_mapping("soil-to-fertilizer", soil)
    water = get_corresponding_from_mapping("fertilizer-to-water", fertilizer)
    light = get_corresponding_from_mapping("water-to-light", water)
    temperature = get_corresponding_from_mapping("light-to-temperature", light)
    humidity = get_corresponding_from_mapping("temperature-to-humidity", temperature)
    location = get_corresponding_from_mapping("humidity-to-location", humidity)

    locations.append(location)

print(locations)
print(min(locations))
