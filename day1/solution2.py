total = 0

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

with open("day1/input", "r") as f:
    for line in f.readlines():
        first_number = ""
        last_number = ""
        for index in range(len(line)):
            number = ""
            if line[index].isdigit():
                number = line[index]
            else:
                for match, char in numbers.items():
                    if line[index:].startswith(match):
                        number = char
                        break
                if number == "":
                    continue
            if first_number == "":
                first_number = number
            last_number = number
        total += int(first_number + last_number)

print(total)
