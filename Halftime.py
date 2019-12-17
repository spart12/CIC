class Halftime:
    def __init__(self, players):
        self.players = players
        self.biggest_deck = self.biggest_deck()
        self.more_spades = self.more_Spades()
        self.Score()
        self.print_score()

    def biggest_deck(self):
        self.biggest = ['', 0]
        for player in self.players.players:
            if player.deck >= self.biggest[1]:
                if player.deck == self.biggest[1]:
                    return None
                self.biggest = [player, player.deck]
        return self.biggest

    def more_Spades(self):
        self.more_s = ['', 0]
        for player in self.players.players:
            self.spades = 0
            for each in player.deck:
                if each[1] == '♠':
                    self.spades += 1
            if self.spades >= self.more_s[1]:
                if self.spades == self.more_s[1]:
                    return None
                self.more_s = [player, self.spades]
        return self.more_s

    def Score(self):
        for player in self.players.players:
            for each in player.deck:
                if each[0] == 'A' or each == '2♠':
                    player.score += 1
                elif each == '10♦':
                    player.score += 2
            if player == self.biggest_deck[0]:
                player.score += 3
            if player == self.more_spades[0]:
                player.score += 1

    def print_score(self):
        for player in self.players.players:
            print(player.name + str(player.score))
        input('\nPress Enter to continue')
