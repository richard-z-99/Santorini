from memento import Memento

class Square():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.occupant = None
        self.level = 0

    # def update_occupant(self):

    # def update_level(self):

    def __str__(self):
        if (self.occupant == None):
            return '{} '.format(self.level)
        else:
            return '{}{}'.format(self.level, self.occupant)


class Board():
    def __init__(self):
        self.squares = self.create_board()
        self.memento = Memento()

    def create_board(self):
        board = []
        for row in range(5):
            new_row = []
            for col in range(5):
                new_row.append(Square(row, col))

    def print_board(self):
        while True:
            print('+--+--+--+--+--+')
            if 
            for square in self.squares:
                print('|')
                print(square)



