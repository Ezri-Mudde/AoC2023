from collections import Counter


total = 0

copies: Counter[int] = Counter()

for i in range(1, 209 + 1):
    copies[i] = 1

with open("day4/input", "r") as f:
    for line in f.readlines():
        card, line = line.split(":")
        card_id = int(card.split(" ")[-1])
        my, winning = line.split("|")
        my_numbers = [
            int(number.strip()) for number in my.split(" ") if number.strip() != ""
        ]
        winning_numbers = [
            int(number.strip()) for number in winning.split(" ") if number.strip() != ""
        ]
        card_copy_count = copies.get(card_id, 1)

        winning_count = 0
        for number in my_numbers:
            if number in winning_numbers:
                winning_count += 1
        for j in range(card_id + 1, card_id + winning_count + 1):
            copies[j] += card_copy_count

print(copies.total())
