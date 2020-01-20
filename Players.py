from Player import Player

class Players:
    def __init__(self):
        self.players = []
        self.play()

    def play(self):
        self.cant_players = input('\nEnter the number of Players: ')
        if self.input_valid(self.cant_players):
            if int(self.cant_players) >= 2 and int(self.cant_players) <= 4:
                i = 1
                while i <= int(self.cant_players):
                    print('\nPlayer ' + str(i))
                    self.player_name = self.Name_valid()
                    self.player_name = Player(self.player_name)
                    self.players.append(self.player_name)
                    i += 1
            else:
                print('\nInvalid value \nValid numbers (2-4)')
                self.play()
        else:
            print('\nInvalid input\nTry again')
            self.play()

    def Name_valid(self):
        self.name = input('Enter your name: ')
        if self.name.isalpha():
            return self.name.capitalize()
        else:
            print('\nInvalid name\nTry again\n')
            self.Name_valid()

    def input_valid(self, element):
        return element.isnumeric()
