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
        input = input('Enter the card position that you wanna drop (e.g.: 2): ')
        aux_position = self.Isnumeric(input)
        if aux_position:
            self.position_player_hand = aux_position
            if self.check_index():
                self.table.append(self.hand[self.position_player_hand])
                self.hand.pop(self.position_player_hand)
            else:
                print('\nPosition out of range\nTry again\n')
                self.Drop_move()

    def Take_move(self):
        self.action2 = input('Enter "1" if you wanna take one card from the table \n"2" for more than one\n')
        self.func_position()
        if self.func_aux_move_valid():
            if self.action2 == '1':
                # Add selected cards to  player's deck
                self.deck += [self.hand[self.position_player_hand], self.table[self.position_table]]
                # Delete those cards
                self.table.pop(self.position_table)
                self.hand.pop(self.position_player_hand)

            elif self.action2 == '2':
                for position_table in self.position_table:
                    self.deck.append(self.table[int(position_table) - 1])
                    self.deck.append(self.hand[self.position_player_hand])

                for i, position_table in enumerate(self.position_table):
                    self.table.pop(int(position_table) - (i + 1))

                self.hand.pop(self.position_player_hand)

    def Call_move(self):
        self.action2 = '1'
        self.func_position()
        if self.func_aux_move_valid():
            #Create a group for easier adding
            self.group = [self.hand[self.position_player_hand], self.table[self.position_table]]
            self.table.pop(self.position_table)
            self.table.insert(self.position_table, self.group)
            self.hand.pop(self.position_player_hand)

    def Build_move(self):
        self.action2 = input('Enter "1" if you wanna build with one card from the table \n"2" for more than one\n')
        self.func_position()
        if self.func_aux_move_valid():
            if self.action2 == '1':
                if type(self.table[self.position_table]) == list:
                    self.group = [self.hand[self.position_player_hand]]
                    for e in self.table[self.position_table]:
                        self.group += [e]
                else:
                    self.group = [self.hand[self.position_player_hand]] + [self.table[self.position_table]]
                self.table.pop(self.position_table)
                self.table.insert(self.position_table, self.group) 
                self.hand.pop(self.position_player_hand)


            elif self.action2 == '2':
                self.group = []
                for position_table in self.position_table:
                    self.group += [self.table[int(position_table) - 1]]
                
                for i, position in enumerate(self.position_table):
                    self.table.pop(int(position_table) - (i + 1))

                self.group += [self.hand[self.position_player_hand]]
                self.table.insert(int(self.position_table[0]) - 1, self.group)
                self.hand.pop(self.position_player_hand)

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
        self.suma = 0
        if self.action2 == '1':
            if type(self.table[self.position_table]) == list:
                self.func_sum(self.table[self.position_table])
                if self.suma == self.Specials_cards(self.hand[self.position_player_hand][:-1]) or self.Multiples(self.Specials_cards(self.hand[self.position_player_hand][:-1]), suma):
                    self.valid = True
            else:
                if self.hand[self.position_player_hand][:-1] == self.table[self.position_table][:-1]:
                    self.valid = True
        else:
            for e in self.position_table:
                e = int(e) - 1
                if type(self.table[e]) == list:
                    self.func_sum(self.table[e])
                else:
                    self.suma += self.Specials_cards(self.table[e][:-1])
            if self.suma == self.Specials_cards(self.hand[self.position_player_hand][:-1]) or self.Multiples(self.hand[self.position_player_hand][:-1], suma):
                self.valid = True
                
    
    def Call_valid(self):
        if self.hand[self.position_player_hand][:-1] == self.table[self.position_table][:-1]:
            self.valid = True

    def Build_valid(self):
        self.suma = 0
        if self.action2 == '1':
            if type(self.table[self.position_table]) == list:
                self.func_sum(self.table[self.position_table])
                self.suma += self.Specials_cards(self.hand[self.position_player_hand][:-1])
            else:
                self.suma = self.Specials_cards(self.hand[self.position_player_hand][:-1]) + self.Specials_cards(self.table[self.position_table][:-1])
            for e in self.hand:
                if self.suma == self.Specials_cards(e[:-1]) or self.Multiples(self.Specials_cards(e[:-1]), self.suma):
                    self.valid = True
        else:
            for e in self.position_table:
                if type(e) != list:
                    self.suma += self.Specials_cards(self.table[int(e)-1][:-1])
            self.suma += self.Specials_cards(self.hand[self.position_player_hand][:-1])

            for e in self.hand:
                if self.suma == self.Specials_cards(e[:-1]) or self.Multiples(self.Specials_cards(e[:-1]), self.suma):
                    self.valid = True

    def check_index(self):
        if self.move != 'drop':
            if type(self.position_table) == list:
                for e in self.position_table:
                    if int(e) - 1 >= len(self.table):
                        return False
            else:
                if self.position_table >= len(self.table):
                    return False
        if self.position_player_hand >= len(self.hand):
            return False
        return True
                    
    def Specials_cards(self, card):
        self.specials_c = {'A':1, 'J': 11, 'Q':12, 'K':13}
        if card in self.specials_c:
            return self.specials_c[card]
        else:
            return int(card)

    def Multiples(self, card, total):
        card_multiple = [card * 2, card * 3, card * 4]
        for e in card_multiple:
            if total == e:
                return True

    def func_sum(self, lst):
        for e in lst:
            self.suma += self.Specials_cards(e[:-1])

    def func_position(self):
        aux_position_table = ''
        aux_position_hand = ''
        if self.action2 == '1':
            aux_position_table = self.Isnumeric(input('Card position from the table (e.g.: 2): '))
        elif self.action2 == '2':
            aux_position_table = self.Isnumeric(input('Cards position from the table, separates by commas (e.g.: 2,3,4): ').split(','))
        else:
            print('\nTry again\n')
            self.func_moves()

        aux_position_hand = self.Isnumeric(input('Card position from your hand (e.g.: 2): '))
        if aux_position_hand and aux_position_table:
            self.position_table = aux_position_table
            self.position_player_hand = aux_position_hand

    def func_aux_move_valid(self):
        if self.check_index():
            if self.cards_valid():
                return True
            else:
                print('\n\nInvalid move \n Try again\n\n')
                self.Move(self.table)
        else:
            print('\nPosition out of range\nTry again\n')
            self.Move(self.table)

    def Isnumeric(self, element):
        if type(element) == list:
            return element
        else:
            if element.isnumeric():
                return int(element) - 1
        self.func_moves()
