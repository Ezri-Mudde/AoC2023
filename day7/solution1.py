from collections import Counter
from typing import List


class Hand:
    card_order: List[str] = [
        "A",
        "K",
        "Q",
        "J",
        "T",
        "9",
        "8",
        "7",
        "6",
        "5",
        "4",
        "3",
        "2",
    ]
    type_order: List[str] = [
        "five of a kind",
        "four of a kind",
        "full house",
        "three of a kind",
        "two pair",
        "one pair",
        "high card",
    ]

    def __init__(self, cards: str, bet: int) -> None:
        self.cards = cards
        self.card_counts = Counter(cards)
        self.bet = bet

    def type(self) -> str:
        cards = self.card_counts.most_common()

        if cards[0][1] == 5:
            return "five of a kind"

        if cards[0][1] == 4:
            return "four of a kind"

        if cards[0][1] == 3 and cards[1][1] == 2:
            return "full house"

        if cards[0][1] == 3:
            return "three of a kind"

        if cards[0][1] == 2 and cards[1][1] == 2:
            return "two pair"

        if cards[0][1] == 2:
            return "one pair"

        return "high card"

    def __lt__(self, other: "Hand") -> bool:
        if self.type_order.index(self.type()) > self.type_order.index(other.type()):
            return True
        elif self.type_order.index(self.type()) < self.type_order.index(other.type()):
            return False

        for i in range(len(self.cards)):
            if self.cards[i] == other.cards[i]:
                continue
            if self.card_order.index(self.cards[i]) > self.card_order.index(
                other.cards[i]
            ):
                return True
            elif self.card_order.index(self.cards[i]) < self.card_order.index(
                other.cards[i]
            ):
                return False


if __name__ == "__main__":
    with open("day7/input", "r") as f:
        hands: List[Hand] = []
        for line in f.readlines():
            cards, bet = line.split(" ")
            hands.append(Hand(cards=cards, bet=int(bet)))

    hands = sorted(hands)

    total = 0
    for i in range(len(hands)):
        hand = hands[i]
        # print(
        #     f"Hand with cards {hand.cards} has type {hand.type()} and rank {i+1} and score {hand.bet * (i + 1)}"
        # )
        total += hand.bet * (i + 1)
    print(total)
