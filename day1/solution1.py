total = 0

with open("day1/input", "r") as f:
    for line in f.readlines():
        first_number = ""
        last_number = ""
        for char in line:
            if not char.isdigit():
                continue
            if first_number == "":
                first_number = char
            last_number = char
        total += int(first_number + last_number)

print(total)
