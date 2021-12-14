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
    def __init__(self, color):
        self.color = color

        if(self.color == 'white'):
            self.worker1 = Worker('A')
            self.worker2 = Worker('B')

        elif(self.color == 'blue'):
            self.worker1 = Worker('Y')
            self.worker2 = Worker('Z')

        else:
            print("ERROR: Invalid player name")




class Human(Player):
    def __init__(self, color):
        super().__init__(color)


class Random(Player):
    def __init__(self, color):
        super().__init__(color)

    



class Worker:
    def __init__(self, name, row=4, col=3):
        self.name = name
        self.row = row
        self.col = col
        
        #initialize worker to default location depending on name
        if(self.name == 'A'):
            self.update_location(3,1)
        
        elif(self.name == 'B'):
            self.update_location(1,3)

        elif(self.name == 'Y'):
            self.update_location(1, 1)

        elif(self.name == 'Z'):
            self.update_location(3, 3)

        else:
            print("ERROR: Invalid worker name")

    def find_legal_moves(self):
        return self.board.find_legal_moves(self)

    def find_legal_builds(self):
        return self.board.find_legal_builds(self)

    def update_location(self, new_row, new_col):
        self.row = new_row
        self.col = new_col



class Square:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.occupant = None
        self.level = 0

    def update_occupant(self, new_occupant = None):
        #if move into square, update occupant. if more out of square, occupant = None.
        if new_occupant is None:
            self.occupant = None
        else:
            self.occupant = new_occupant

    def update_level(self):
        #if level < 4, build up 1 level.
        if self.level < 4:
            self.level += 1
        # else:
        #     print("Cannot build {}".format(self.direction))

    def __str__(self):
        if (self.occupant == None):
            return '|{} '.format(self.level)
        else:
            return '|{}{}'.format(self.level, self.occupant.name)



class Board:
    def __init__(self, color):
        self.white_player = Player("white")
        self.blue_player = Player("blue")
        self.squares = self.create_board()
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
        #print("hello")
        return board



    def print_board(self):
        for i in range(5):
            print('+--+--+--+--+--+')
            s=""
            for j in range(5):
                s += str(self.squares[i][j])
            s += '|'
            print(s)
        print('+--+--+--+--+--+')



    def get_square(self, row, col):
        return self.squares[row][col]



class Action:
    def __init__(self, direction, worker):
        self.direction = direction
        self.worker = worker

    def get_new_coords(self):
        curr_row = self.worker.row
        curr_col = self.worker.col
        new_row = curr_row + directions.get(self.direction)[0]
        new_col = curr_col + directions.get(self.direction)[1]
        return [new_row, new_col]



class Move(Action):
    def __init__(self, direction, worker):
        super().__init__(direction, worker)


class Build(Action):
    def __init__(self, direction, worker):
        super().__init__(direction, worker)
