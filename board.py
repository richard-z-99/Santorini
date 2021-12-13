from memento import Memento
from player import Player

directions = { 'n': (-1,0)), 'ne': (-1,1), 'e': (0,1), 'se': (1,1), 's': (1,0), 'sw': (1,-1), 'w': (0, -1), 'nw': (-1, -1)}

class Square:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.occupant = None
        self.level = 0

    # def update_occupant(self):

    # def update_level(self):

    def __str__(self):
        if (self.occupant == None):
            return '|{} '.format(self.level)
        else:
            return '|{}{}'.format(self.level, self.occupant)

class Board:
    def __init__(self, color):
        self.squares = self.create_board()
        self.memento = Memento()
        self.white_player = Player(self.memento, "white", self)
        self.blue_player = Player(self.memento, "blue", self)
        self.color = color
        if self.color == "white":
            self.curr_player = self.white_player
        if self.color == "blue":
            self.curr_player = self.blue_player

    def create_board(self):
        #create 2d array board w/o borders
        board = []
        for row in range(5):
            new_row = []
            for col in range(5):
                new_row.append(Square(row, col))
                board.append(new_row)
        return board

    def print_board(self):
        i = 0
        j = 0
        while i < 5:
            print('+--+--+--+--+--+')
            i+=1
            while j < 5:
                self.squares[i][j]
                j+=1
            if j == 5:
                print('|')
        print('+--+--+--+--+--+')

    def _check_level(self, move):
        #can move 1 level up, any number of levels down. Cannot move onto level 4.
        if move.worker.location.level - move.worker.level <= 1 and new_square.level != 4:
            return True
        else:
            return False

    def execute_move(self, move):
        pass

class Action:
    # def __init__(self, board, new_square, worker):
    # #'worker contains old square. board = current board state.
    #     self.board = board
    #     self.new_square = new_square
    #     self.worker = worker

    def __init__(self, board, direction, worker):
    #'worker contains old square. board = current board state.
        self.board = board
        self.direction = direction
        self.worker = worker

    def execute(self):
        pass

    def _check_level(self, move):
        #can move 1 level up, any number of levels down. Cannot move onto level 4.
        if move.worker.location.level - move.worker.level <= 1 and new_square.level != 4:
            return True
        else:
            return False


class Move(Action):
    # def __init__(self, board, new_square, worker):
    #     super().__init__(board, new_square, worker)

    def __init__(self, board, direction, worker):
        super().__init__(board, direction, worker)

    def execute(self):
        #passing in self Move object
        self.board.execute_move(self)
