from santorini_classes import Action, Build, HumanPlayer, RandomPlayer, Move
from board import Board
import copy
import sys

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
    def __init__(self, kind1, kind2):
        #initialize default board
        board = Board(kind1, kind2, "white")
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


        #TODO: Error checking on move_direction, actually moving worker. DONE, i think
        
        move_dir = input("Select a direction to move {}\n".format(directions.keys()))
        move = Move(move_dir, worker)
        if(game.check_move(move)):
            game.execute_move(move)


        #TODO: implement build. DONE, i think
        build_dir = input("Select a direction to build {}\n".format(directions.keys()))
        build = Build(build_dir, worker)
        #no other checks on building besides check_board.
        if (game.check_build(build)):
            game.execute_build(build)



class PlayGame:
    def __init__(self, kind1, kind2):
        self.memento = Memento(kind1, kind2)
        self.kind1 = kind1
        self.kind2 = kind2

        #keeps track of current board
        self.board = self.memento.history[self.memento.cur_board]


    def print_curr_board(self):
        self.board.print_board()
        #print("TODO: print turn/player information")


    def undo(self):
        self.memento.undo()
        self.update_board()

    def redo(self):
        self.memento.redo()
        self.update_board()

    
    def run(self):
        #change while condition to not_win later
        while self.board.check_won(self.board.curr_player) is False:
            if isinstance(self.board.curr_player, HumanPlayer):
                self.print_curr_board()
                curr_worker = self.board.curr_player.choose_worker()
                legal_moves = self.board.get_legal_moves(self.board.curr_player)
                move = self.board.curr_player.choose_move(legal_moves, curr_worker)
                self.execute_move(move)
                legal_builds = self.board.get_legal_builds(self.board.curr_player, move.worker)
                build = self.board.curr_player.choose_build(legal_builds, curr_worker)
                self.execute_build(build)
                self.board.switch_player()

        #if bot
            else:
                self.print_curr_board()
                legal_moves = self.board.get_legal_moves(self.board.curr_player)
                move = self.board.curr_player.choose_move(legal_moves)
                self.execute_move(move)
                legal_builds = self.board.get_legal_builds(self.board.curr_player, move.worker)
                build = self.board.curr_player.choose_build(legal_builds)
                self.execute_build(build)
                self.board.switch_player()
                print("NEW TURN")
            #bot choose move will not have curr worker. also choose_build. Curr_worker is just a property of the legal_move that was chosen by the algo
        #change curr_player, iterate turn =+1. Can implement in execute_build


    def execute_move(self, move):
        #make copy of old board and put into memento
        self.update_board()
        old_board_copy = copy.deepcopy(self.board)
        self.memento.history[self.memento.cur_board] = old_board_copy

        self.board.execute_move(move)

        # #update location of worker
        # old_row = move.worker.row
        # old_col = move.worker.col
        # new_row = move.get_new_coords()[0]
        # new_col = move.get_new_coords()[1]

        # move.worker.update_location(new_row, new_col)

        # #update occupancy status of old/new squares
        # old_square = self.board.get_square(old_row, old_col)
        # old_square.update_occupant(None)

        # new_square = self.board.get_square(new_row, new_col)
        # new_square.update_occupant(move.worker)




    def execute_build(self, build):
        # new_row = build.get_new_coords()[0]
        # new_col = build.get_new_coords()[1]

        # #update level of new_square
        # #in main, need to check if valid build (not building above level 4)
        # new_square = self.board.get_square(new_row, new_col)
        # new_square.update_level()

        self.board.execute_build(build)

        #update memento
        self.memento.next(self.board)
        self.update_board()



    def update_board(self):
        self.board = self.memento.history[self.memento.cur_board]
        
if __name__ == "__main__":
    kind1 = sys.argv[1]
    kind2 = sys.argv[2]

    game1 = PlayGame(kind1, kind2)
    game1.run()
