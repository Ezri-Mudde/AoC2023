from typing import List, TypedDict


class Race(TypedDict):
    duration: int
    record: int


def parse_input(lines: List[str]) -> List[Race]:
    time_line = lines[0].split(":")[-1].strip()
    record_line = lines[1].split(":")[-1].strip()

    times = time_line.split()
    records = record_line.split()

    races: List[Race] = []

    time = ""
    record = ""

    for i in range(len(times)):
        time += times[i].strip()
        record += records[i].strip()

    races.append(Race(duration=int(time), record=int(record)))

    return races


def calculate_possible_times(race: Race) -> List[int]:
    possible_times: List[int] = []

    for hold_time in range(race["duration"]):
        distance = (race["duration"] - hold_time) * hold_time
        if distance > race["record"]:
            possible_times.append(hold_time)

    return possible_times


if __name__ == "__main__":
    with open("day6/input", "r") as f:
        races = parse_input(f.readlines())

        possible_times_lists = [calculate_possible_times(race) for race in races]

        total = len(possible_times_lists[0])

        for possible_time_list in possible_times_lists[1:]:
            total = total * len(possible_time_list)

        print(total)
