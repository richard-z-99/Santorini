directions = { 
    'n': (-1,0), 
    'ne': (-1,1), 
    'e': (0,1), 
    'se': (1,1), 
    's': (1,0), 
    'sw': (1,-1), 
    'w': (0, -1), 
    'nw': (-1, -1)
    }

class Player:
    def __init__(self, memento, color, board):
        self.memento = memento
        self.color = color
        self.board = board

        if(self.color == 'white'):
            self.worker1 = Worker(self, 'A')
            self.worker2 = Worker(self, 'B')

        elif(self.color == 'blue'):
            self.worker1 = Worker(self, 'Y')
            self.worker2 = Worker(self, 'Z')

        else:
            print("ERROR: Invalid player name")




class Human(Player):
    def __init__(self, memento, color, board):
        super().__init__(memento, color, board)



class Worker:
    def __init__(self, player, name):
        self.player = player
        self.name = name
        self.board = player.board
        
        #initialize worker to default location depending on name
        if(self.name == 'A'):
            self.update_location(self.board.squares[1][3])
        
        elif(self.name == 'B'):
            self.update_location(self.board.squares[3][1])

        elif(self.name == 'Y'):
            self.update_location(self.board.squares[1][1])

        elif(self.name == 'Z'):
            self.update_location(self.board.squares[3][3])

        else:
            print("ERROR: Invalid worker name")


    def find_legal_moves(self):
        return self.board.find_legal_moves(self)


    def find_legal_builds(self):
        return self.board.find_legal_builds(self)


    def update_location(self, new_square):
        self.location = new_square
        new_square.update_occupant(self)






class Square:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.occupant = None
        self.level = 0

    def update_occupant(self):
        pass

    def update_level(self):
        pass

    def __str__(self):
        if (self.occupant == None):
            return '|{} '.format(self.level)
        else:
            return '|{}{}'.format(self.level, self.occupant)


class Board:
    def __init__(self, color):
        self.squares = self.create_board()
        self.white_player = Player("white")
        self.blue_player = Player("blue")
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
        
        
    def get_square(self, row, col):
        return self.squares[row][col]




class Action:
    def __init__(self, direction, worker):
        self.direction = direction
        self.worker = worker



class Move(Action):
    def __init__(self, direction, worker):
        super().__init__(direction, worker)
