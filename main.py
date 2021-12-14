from santorini_classes import Board, Action, Move
import copy


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


class Memento:
    def __init__(self):
        #initialize default board
        board = Board("white")
        board.get_square(3,1).occupant = board.white_player.worker1
        board.get_square(1,3).occupant = board.white_player.worker2
        board.get_square(1,1).occupant = board.blue_player.worker1
        board.get_square(3,3).occupant = board.blue_player.worker2

        self.history = [board]
        self.cur_board = 0
    
    def undo(self):
        if(self.cur_board > 0):
            self.cur_board -= 1

    def redo(self):
        if(self.cur_board < len(self.history)-1):
            self.cur_board += 1

    def next(self, new_board):
        self.history[:self.cur_board+1]
        self.history.append(new_board)
        self.cur_board += 1




class RunHuman:
    def run(self):
        worker_name = input("Select a worker to move\n>")
        if(worker_name == 'A'): 
            worker = self.worker1

        elif(worker_name == 'B'):
            worker = self.worker2

        else:
            print("Invalid worker name input")
            return

        #TODO: Error checking on move_direction, actually moving worker
        move_dir = input("Select a direction to move {}\n".format(directions.keys()))

        if(not directions.has_key(move_dir)):
            print("Invalid move input")
            return

        else:
            pass


        #TODO: Error checking on build_direction, actually building
        build_dir = input("Select a direction to build {}}\n".format(directions.keys()))






class PlayGame:
    def __init__(self):
        self.memento = Memento()

        #keeps track of most current board
        self.board = self.memento.history[self.memento.cur_board]


    def undo(self):
        self.memento.undo()
        self.board = self.memento.history[self.memento.cur_board]

    def redo(self):
        self.memento.redo()
        self.board = self.memento.history[self.memento.cur_board]
        
    
    def run(self):
        pass
    
    #returns true if action stays on board and new square is unoccupied
    def check_board(self, action):
        self.board = self.memento.history[self.memento.cur_board]
        new_row = action.get_new_coords()[0]
        new_col = action.get_new_coords()[1]

        if (0 <= new_row < 5 and 0 <= new_col < 5):
            occupant = self.board.get_square(new_row, new_col).occupant
            return (occupant is None)

        else:
            return False


    #checks if move is valid
    def check_move(self, move):
        self.board = self.memento.history[self.memento.cur_board]
        if(not self.check_board(move)):
            return False

        new_row = move.get_new_coords()[0]
        new_col = move.get_new_coords()[1]
        old_row = move.worker.row
        old_col = move.worker.col
        
        old_level = self.board.get_square(old_row, old_col).level
        new_level = self.board.get_square(new_row, new_col).level
        return (new_level < 4 and new_level-old_level <= 1)


    def execute(self, move):
        #save a copy of current board before doing anything else
        self.board = self.memento.history[self.memento.cur_board]
        old_board_copy = copy.deepcopy(self.board)

        old_row = move.worker.row
        old_col = move.worker.col
        new_row = move.get_new_coords()[0]
        new_col = move.get_new_coords()[1]

        #update location of worker
        move.worker.update_location(new_row, new_col)

        #update occupancy status of old/new squares
        old_square = self.board.get_square(old_row, old_col)
        old_square.update_occupant(None)

        new_square = self.board.get_square(new_row, new_col)
        new_square.update_occupant(move.worker)

        new_board = copy.deepcopy(self.board)

        #put old board copy into memento
        self.memento.history[self.memento.cur_board] = old_board_copy

        #add new board to memento and update self.board
        self.memento.next(new_board)
        self.board = self.memento.history[self.memento.cur_board]
        
