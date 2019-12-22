import random

class Poker_cards:
    def __init__(self):
        self.poker = self.cards()
        random.shuffle(self.poker)

    def cards(self):
        nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        symbols = ['♥', '♦', '♣', '♠']
        self.cards = []
        for num in nums:
            for symb in symbols:
                self.cards.append(num+symb)
        return self.cards
