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
    #outputs instructions for human player, reads input, and executes corresponding move
    def run(self, game):
        player = game.board.curr_player

        #TODO: loop until valid name inputted

        worker_name = input("Select a worker to move\n>")
        if(worker_name == player.worker1.name): 
            worker = player.worker1

        elif(worker_name == player.worker2.name):
            worker = player.worker2


        #TODO: Error checking on move_direction, actually moving worker
        
        move_dir = input("Select a direction to move {}\n".format(directions.keys()))
        move = Move(worker, move_dir)
        if(game.check_move(move)):
            game.execute_move(move)


        #TODO: implement build 






class PlayGame:
    def __init__(self):
        self.memento = Memento()

        #keeps track of current board
        self.board = self.memento.history[self.memento.cur_board]


    def undo(self):
        self.memento.undo()
        self.update_board()

    def redo(self):
        self.memento.redo()
        self.update_board()

    
    def run(self):
        pass
    
    #returns true if action stays on board and new square is unoccupied
    def check_board(self, action):
        self.update_board()
        new_row = action.get_new_coords()[0]
        new_col = action.get_new_coords()[1]

        if (0 <= new_row < 5 and 0 <= new_col < 5):
            level = self.board.get_square(new_row, new_col).level
            occupant = self.board.get_square(new_row, new_col).occupant
            return (occupant is None and level < 4)

        else:
            return False


    #checks if move is valid
    def check_move(self, move):
        self.update_board()
        if(not self.check_board(move)):
            return False

        new_row = move.get_new_coords()[0]
        new_col = move.get_new_coords()[1]
        old_row = move.worker.row
        old_col = move.worker.col
        
        old_level = self.board.get_square(old_row, old_col).level
        new_level = self.board.get_square(new_row, new_col).level
        return (new_level < 4 and new_level-old_level <= 1)



    #executes a move then a build, saves everything to memento
    def execute_turn(self, move, build):
        #save copy of old board
        self.update_board()
        old_board_copy = copy.deepcopy(self.board)

        #perform move/build
        self.execute_move(move)
        self.execute_build(build)

        #update memento
        #new_board = copy.deepcopy(self.board)
        self.memento.history[self.memento.cur_board] = old_board_copy
        #self.memento.next(new_board)
        self.memento.next(self.board)
        self.update_board()





    def execute_move(self, move):
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


    def execute_build(self, build):
        new_row = build.get_new_coords()[0]
        new_col = build.get_new_coords()[1]

        #update level of new_square
        #in main, need to check if valid build (not building above level 4)
        new_square = self.board.get_square(new_row, new_col)
        new_square.update_level()



    def update_board(self):
        self.board = self.memento.history[self.memento.cur_board]
        
