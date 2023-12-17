class Hand:
    card_order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A", ]

    def __init__(self, line: str) -> None:
        # line is in format "AQK32 123", a hand of cards and an integer bid-value
        self.cards, self.bid = line.split(" ")
        self.bid = int(self.bid)
        self.frequency_map: dict[str, int] = dict(sorted({char: self.cards.count(char) for char in set(self.cards)}.items(), key=lambda x: x[1], reverse=True))
        self.hand_type = self.determine_hand_type()

    def determine_hand_type(self) -> int:
        # Sort frequencies in descending order
        sorted_frequencies: tuple[int] = tuple(self.frequency_map.values())

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
        return hand_types.get(sorted_frequencies, -1)

    def __str__(self):
        return f"{self.cards} {self.bid}"

    def __eq__(self, other) -> bool:
        return self.cards == other.cards

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
                return self.card_order.index(self_card) > self.card_order.index(other_card)
        return False


class JokerHand(Hand):
    card_order = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A", ]

    def __init__(self, line: str):
        # line is in format "AQK32 123", a hand of cards and an integer bid-value
        super().__init__(line)

        # add Jokers to other max card frequency
        if "J" in self.frequency_map and self.frequency_map["J"] != 5:
            J_value = self.frequency_map.pop("J")
            max_key = max(self.frequency_map, key=self.frequency_map.get)
            self.frequency_map[max_key] += J_value
        # determine hand type again
        self.hand_type = self.determine_hand_type()


FILE_DIR = "../input_files"

if __name__ == '__main__':
    normal_hands = []
    joker_hands = []
    # read input, create lists of hands
    with open("%s/Day7Input.txt" % FILE_DIR, "r") as advent_file:
        for line in advent_file:
            normal_hands.append(Hand(line.strip()))
            joker_hands.append(JokerHand(line.strip()))

    # sort hands
    sorted_hands = sorted(normal_hands)
    sorted_joker_hands = sorted(joker_hands)

    # calculate sums and print them

    bid_sum = 0
    for i, hand in enumerate(sorted_hands, start=1):
        bid_sum += i * hand.bid
    print("Part 1:", bid_sum)
    bid_sum = 0
    for i, hand in enumerate(sorted_joker_hands, start=1):
        bid_sum += i * hand.bid
    print("Part 2:", bid_sum)



