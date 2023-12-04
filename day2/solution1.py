from typing import Any, List


games: List[dict[str, Any]] = []

with open("day2/input", "r") as f:
    for line in f.readlines():
        game = {
            "id": "",
            "rounds": [],
        }
        parts = line.split(":")
        game["id"] = parts[0].split(" ")[-1]

        rounds = parts[-1].split(";")

        for round in rounds:
            cubes = round.split(",")
            game_round = {
                "red": 0,
                "blue": 0,
                "green": 0,
            }
            for cube in cubes:
                count, color = cube.strip().split(" ")
                game_round[color] += int(count)
            game["rounds"].append(game_round)
        games.append(game)

total = 0

for game in games:
    possible = True
    for round in game["rounds"]:
        if round["red"] > 12 or round["green"] > 13 or round["blue"] > 14:
            possible = False
            break
    if possible:
        total += int(game["id"])

print(total)
