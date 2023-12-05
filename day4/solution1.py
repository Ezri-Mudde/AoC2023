total = 0

with open("day4/input", "r") as f:
    for line in f.readlines():
        line = line.split(":")[-1]
        my, winning = line.split("|")
        my_numbers = [
            int(number.strip()) for number in my.split(" ") if number.strip() != ""
        ]
        winning_numbers = [
            int(number.strip()) for number in winning.split(" ") if number.strip() != ""
        ]

        winning_count = -1
        for number in my_numbers:
            if number in winning_numbers:
                winning_count += 1

        if winning_count >= 0:
            total += pow(2, winning_count)

print(total)
