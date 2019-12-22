class Dealer:
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players
    
    def deal(self):
        # Deal two cards at time
        for player in self.players:
            self.nt = self.deck[-2:]
            player.hand += self.nt
            del self.deck[-2:]
