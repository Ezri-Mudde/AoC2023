total = 0

with open("day2/input", "r") as f:
    for line in f.readlines():
        game = {
            "id": "",
            "cubes": {
                "red": 0,
                "blue": 0,
                "green": 0,
            },
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
            for color in game["cubes"].keys():
                game["cubes"][color] = max(game["cubes"][color], game_round[color])

        total += game["cubes"]["red"] * game["cubes"]["blue"] * game["cubes"]["green"]

print(total)
