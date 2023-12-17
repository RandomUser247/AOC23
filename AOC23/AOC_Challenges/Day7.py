class Hand:
    card_order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A",]

    def __init__(self, line: str) -> None:
        # line is in format "AQK32 123", a hand of cards and an integer bid-value
        self.cards, self.bid = line.split(" ")
        self.bid = int(self.bid)
        self.frequency_map = {char: self.cards.count(char) for char in set(self.cards)}
        self.hand_type = self.determine_hand_type()

    def determine_hand_type(self) -> int:
        # Sort frequencies in descending order
        sorted_frequencies: list[int] = sorted(self.frequency_map.values(), reverse=True)

        # Define a dictionary mapping sorted frequency tuples to hand types
        hand_types = {
            (5,): 6,  # 5 of a kind
            (4, 1): 5,  # 4 of a kind
            (3, 2): 4,  # Full house
            (3, 1, 1): 3,  # 3 of a kind
            (2, 2, 1): 2,  # Two pair
            (2, 1, 1, 1): 1,  # One pair
            (1, 1, 1, 1, 1): 0  # High card
        }
        # Return the corresponding hand type based on the sorted frequencies
        return hand_types.get(tuple(sorted_frequencies), -1)

    def __str__(self):
        return f"{self.cards} {self.bid}"

    def __eq__(self, other) -> bool:
        return self.cards == other.parts

    def __lt__(self, other) -> bool:
        if self.hand_type != other.hand_type:
            return self.hand_type < other.hand_type
        for self_card, other_card in zip(self.cards, other.cards):
            if self_card != other_card:
                return self.card_order.index(self_card) < self.card_order.index(other_card)
        return False

    def __gt__(self, other) -> bool:
        if self.hand_type != other.hand_type:
            return self.hand_type > other.hand_type
        for self_card, other_card in zip(self.cards, other.cards):
            if self_card != other_card:
                return self.card_order.index(self_card) < self.card_order.index(other_card)
        return False

class JokerHand(Hand):
    def __init__(self, line: str):
        # line is in format "AQK32 123", a hand of cards and an integer bid-value
        self.cards, self.bid = line.split(" ")
        self.bid = int(self.bid)
        self.frequency_map = {char: self.cards.count(char) for char in set(self.cards)}
        self.hand_type = self.determine_hand_type()


FILE_DIR = "../input_files"

if __name__ == '__main__':
    with open("%s/Day7Input.txt" % FILE_DIR, "r") as advent_file:
        file_content = [Hand(line.strip()) for line in advent_file]

    sorted_hands = sorted(file_content)
    bid_sum = 0
    for i, hand in enumerate(sorted_hands, start = 1):
        bid_sum += i * hand.bid

    print(bid_sum)