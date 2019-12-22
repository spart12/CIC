class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.deck = []
        self.score = 0

    def Move(self, table):
        self.table = table
        self.move = input('Enter your move (build, call, take, drop): ').lower()
        # Verify if is a valid move
        if self.move_valid():
            self.func_moves()
        else:
            print('\nInvalid input\n')
            self.Move(self.table)

    def move_valid(self):
        self.moves = ['build', 'call', 'take', 'drop']
        self.valid = False
        for each in self.moves:
            if self.move == each:
                self.valid = True
        return self.valid

    def func_moves(self):
        moves = {
            'build': self.Build_move,
            'call': self.Call_move,
            'take': self.Take_move,
            'drop': self.Drop_move
        }
        moves[self.move]()

#/////////////Moves' functions ////////////////////////////////////////////////////////////////////////////////
    def Drop_move(self):
        self.position_player_hand = int(input('Enter the card position that you wanna drop (e.g.: 2): '))
        self.table.append(self.hand[self.position_player_hand)-1]
        self.hand.pop(self.position_player_hand)-1

    def Take_move(self):
        self.action2 = input('Enter "1" if you wanna take one card from the table \n"2" for more than one\n')
        if self.action2 == '1':
            self.position_player_hand = int(input('Card position from your hand (e.g.: 2): '))
            self.position_table = int(input('Card position from the table (e.g.: 2): '))
            if self.cards_valid():
                # Add selected cards to  player's deck
                self.deck += [self.hand[int(self.position_player_hand)-1], self.table[int(self.position_table)-1]]
                # Delete those cards
                self.table.pop(self.position_table-1)
                self.hand.pop(self.position_player_hand-1)

            else:
                print('\n\nInvalid move \n Try again\n\n')
                self.Move(self.table)
        else:
            self.position_player_hand = int(input('Card position from your hand (e.g.: 2): '))
            self.position_table = input('Cards position from the table, separates by commas (e.g.: 2,3,4): ').split(',')
            if self.cards_valid():
                for position_table in self.position_table:
                    self.deck.append(self.table[int(position_table)-1])
                self.deck.append(self.hand[self.position_player_hand-1])

                for i, position_table in enumerate(self.position_table):
                    self.table.pop(int(position_table) - i + 1)
                self.hand.pop(self.position_player_hand-1)

            else:
                print('\n\nInvalid move \n Try again\n\n')
                self.Move(self.table)

    def Call_move(self):
        self.position_player_hand = int(input('Card position from your hand ( e.g.: 2): '))
        self.position_table = int(input('Card position from the table ( e.g.: 2): '))
        if self.cards_valid():
            #Create a group for easier adding
            self.group = [self.hand[self.position_player_hand-1], self.table[int(self.position_table)-1]]
            self.table.pop(self.position_table-1)
            self.table.insert(self.position_table-1, self.group)
            self.hand.pop(self.position_player_hand-1)

        else:
            print('\n\nInvalid move \n Try again\n\n')
            self.Move(self.table)

    def Build_move(self):
        self.action2 = input('Enter "1" if you wanna build with one card from the table \n"2" for more than one\n')
        if self.action2 == '1':
            self.position_player_hand = int(input('Card position from your hand (e.g.: 2): '))
            self.position_table = int(input('Card position from the table (e.g.: 2): '))
            if self.cards_valid():
                if type(self.table[self.position_table-1]) == list:
                    self.group = [self.hand[self.position_player_hand-1]]
                    for e in self.table[self.position_table-1]:
                        self.group += [e]
                else:
                    self.group = [self.hand[self.position_player_hand-1]] + [self.table[self.position_table-1]]
                self.table.pop(self.position_table-1)
                self.table.insert(self.position_table-1, self.group) 
                self.hand.pop(self.position_player_hand-1)

            else:
                print('\n\nInvalid move \n Try again\n\n')
                self.Move(self.table)

        else:
            self.position_player_hand = int(input('Card position from your hand (e.g.: 2): '))
            self.position_table = input('Cards position from the table, separates by commas (e.g.: 2,3,4): ').split(',')
            if self.cards_valid():
                self.group = []
                for position_table in self.position_table:
                    self.group += [self.table[int(position_table) - 1]]
                for i, position in enumerate(self.position_table):
                    self.table.pop(int(position_table) - i + 1 )

                self.group += [self.hand[self.position_player_hand-1]]
                self.table.insert(int(self.position_table[0]) - 1, self.group)
                self.hand.pop(self.position_player_hand - 1)

            else:
                print('\n\nInvalid move \n Try again\n\n')
                self.Move(self.table)

    def cards_valid(self):
        self.valid = False
        moves_valid = {
            'build': self.Build_valid,
            'call': self.Call_valid,
            'take': self.Take_valid
        }
        moves_valid[self.move]()
        return self.valid

#/////////////Moves validation functions //////////////////////////////////////////////////////////////////////////

    def Take_valid(self):
        if self.action2 == '1':
            if type(self.table[self.position_table-1]) == list:
                suma = 0
                same = self.table[self.position_table-1][0][:-1]
                for each in self.table[self.position_table-1]:
                    each = int(each)
                    suma += self.Specials_cards(each[:-1])
                    if each[:-1] != same:
                        same = 0
                if suma == self.Specials_cards(self.hand[self.position_player_hand-1][:-1]) or same == self.hand[self.position_player_hand-1][:-1]:
                    self.valid = True
            else:
                if self.hand[self.position_player_hand-1][:-1] == self.table[self.position_table-1][:-1]:
                    self.valid = True
        else:
            suma = 0
            same = self.table[int(self.position_table[0])-1][:-1]
            for e in self.position_table:
                e = int(e)
                if self.table[e-1][:-1] != self.hand[self.position_player_hand-1][:-1]:
                    suma += self.Specials_cards(self.table[int(e)-1][:-1])
                if self.table[e-1][:-1] != same:
                    same = 0
            if suma == self.Specials_cards(self.hand[self.position_player_hand-1][:-1]) or same == self.hand[self.position_player_hand-1][:-1]:
                self.valid = True
                
    
    def Call_valid(self):
        if self.hand[self.position_player_hand-1][:-1] == self.table[self.position_table-1][:-1]:
            self.valid = True

    def Build_valid(self):
        if self.action2 == '1':
            suma = self.Specials_cards(self.hand[self.position_player_hand-1][:-1]) + self.Specials_cards(self.table[self.position_table-1][:-1])
            for e in self.hand:
                if suma == self.Specials_cards(e[:-1]):
                    self.valid = True
        else:
            suma = 0
            suma2 = 0
            for e in self.position_table:
                suma += self.Specials_cards(self.table[int(e)-1][:-1])
            suma += self.Specials_cards(self.hand[self.position_player_hand-1][:-1])
            suma2 = suma / 2
            for e in self.hand:
                if suma == self.Specials_cards(e[:-1]) or suma2 == self.Specials_cards(e[:-1]):
                    self.valid = True
                    
    def Specials_cards(self, card):
        self.specials_c = {'A':1, 'J': 11, 'Q':12, 'K':13}
        if card in self.specials_c:
            return self.specials_c[card]
        else:
            return card