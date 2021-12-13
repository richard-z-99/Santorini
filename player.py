from memento import Memento
from santorini import Board, Square

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


    def run(self):
        pass



class Human(Player):
    def __init__(self, memento, color, board):
        super().__init__(memento, color, board)

    def run(self):
        pass



class Worker:
    def __init__(self, player, name):
        self.player = player
        self.name = name
        self.board = player.board
        
        #initialize worker to default location depending on name
        if(self.name == 'A'):
            self.update_location(self.board[1][3])
        
        elif(self.name == 'B'):
            self.update_location(self.board[3][1])

        elif(self.name == 'Y'):
            self.update_location(self.board[1][1])

        elif(self.name == 'Z'):
            self.update_location(self.board[3][3])

        else:
            print("ERROR: Invalid worker name")


    def find_legal_moves(self):
        return self.board.find_legal_moves(self)


    def find_legal_builds(self):
        return self.board.find_legal_builds(self)


    def update_location(self, new_square):
        self.location = new_square
        new_square.update_occupant(self)
