# import only system from os 
from os import system, name

from time import sleep
# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
        
from Poker_Cards import Poker_cards
from Halftime import Halftime
from Players import Players
from Player import Player
from Dealear import Dealer

class Casino:
    def __init__(self):
        clear()
        self.Welcome = 'Welcome to Casino Game'
        input(self.Welcome.center(125, '-') + '\n \nPress Enter to continue :) ')
        self.deck = Poker_cards()
        self.players = Players()
        self.dealer = Dealer(self.deck.poker, self.players.players)
        self.table = []
        self.table_set_up()
        self.Game()

    def table_set_up(self):
        while len(self.table) < 4:
            self.dealer.deal()
            self.next = self.deck.poker[-2:]
            self.table += self.next
            del self.deck.poker[-2:]

    def Game(self):
        while self.players.players[-1].hand != []:
            for player in self.players.players:
                clear()
                input(player.name + '\'s turn \nPress Enter to view your hand ')
                clear()
                table = 'Cards in table: ' + str(self.table)
                print(table + '\n' + player.name + '\'s hand: ' + str(player.hand) + '\n')
                player.Move(self.table)

        if self.deck.poker != []:
            self.dealer.deal()
            self.dealer.deal()
            self.Game()
        else:
            # Add the all remaining cards from the table to the player who took cards last
            if self.table != []:
                self.Remaining_cards()
            # Count the points
            Halftime(self.players.players)
            # Check if is necesary another round
            self.One_more()

    def end(self, winner):
        for player in self.players.players:
            message = player.name + str(player.score)
            if player == winner:
                message += ' WINNER!!!')
            print(message)

    def Remaining_cards(self):
        for i in range(len(self.players.players)-1, -1, -1):
            player = self.players.players[i]
            if player == 'take':
                player.deck += self.table

    def One_more(self):
        one_more = True
        for player in self.players.players:
            if player.score >= 21:
                one_more = False
                self.end(player)
        if one_more:
            print('Next Round'.center(125, '-'))
            self.deck = Poker_Cards()
            self.table_set_up()
            self.Game()

game = Casino()
