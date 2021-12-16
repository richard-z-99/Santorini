import random

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

cardinal_directions = "(n, ne, e, se, s, sw, w, nw)"


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

    def choose_move(self, legal_moves):
        pass

    def choose_build(self, legal_builds):
        pass
    
    def choose_worker(self):
        pass

    
class PlayerFactory():
    def create_player(self, kind, color):
        if (kind == "human"):
            return HumanPlayer(color)
        if (kind == "random"):
            return RandomPlayer(color)
        if (kind == "heuristic"):
            return HeuristicPlayer(color)
        
        
class HumanPlayer(Player):
    def __init__(self, color):
        super().__init__(color)

    #returns chosen worker of curr player
    def choose_worker(self):
        while True:
            worker_name = input("Select a worker to move\n")
            if(worker_name == self.worker1.name): 
                worker = self.worker1
                return worker
            elif(worker_name == self.worker2.name):
                worker = self.worker2
                return worker
            elif(worker_name not in ['A', 'B', 'Y', 'Z']):
                print("Not a valid worker")
            elif(worker_name not in [self.worker1.name or self.worker2.name]):
                print("That is not your worker")
    
    #legal_moves generated by calling get_legal_moves() in Board
    def choose_move(self, legal_moves, worker):
        while True:
            move_dir = input("Select a direction to move {}\n".format(cardinal_directions))
            if(not move_dir in directions.keys()):
                print("Not a valid direction")
            else:
                move = Move(move_dir, worker)
                valid_move = False
                for item in legal_moves:
                    if (item == move):
                        valid_move = True
                if not valid_move:
                    print("Cannot move {}".format(move_dir))
                else:
                    return move

    #legal_builds generated by calling get_legal_builds() in Board
    def choose_build(self, legal_builds, worker):
        while True:
            # cardinal_dir = list(directions.keys())
            # res = str(test_list)[1:-1]
            build_dir = input("Select a direction to build {}\n".format(cardinal_directions))
            if(build_dir not in directions.keys()):
                print("Not a valid direction")
            else:
                build = Build(build_dir, worker)
                valid_build = False
                # print(len(legal_builds))
                for item in legal_builds:
                    if item == build:
                        valid_build = True
                if not valid_build:
                    print("Cannot build {}".format(build_dir))
                else:
                    return build

class RandomPlayer(Player):
    def __init__(self, color):
        super().__init__(color)

    #legal_moves generated by calling get_legal_moves() in PlayGame
    def choose_move(self, legal_moves):
        move = random.choice(legal_moves)
        return move

    #legal_builds generated by calling get_legal_builds() in PlayGame
    def choose_build(self, legal_builds):
        build = random.choice(legal_builds)
        return build




class HeuristicPlayer(Player):
    def __init__(self, color):
        super().__init__(color)

    def choose_move(self, legal_moves):
        pass 

    def choose_build(self, legal_builds):
        pass
    



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

    # def find_legal_moves(self):
    #     return self.board.find_legal_moves(self)

    # def find_legal_builds(self):
    #     return self.board.find_legal_builds(self)

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

    def __eq__(self, other):
        return self.direction == other.direction and self.worker.name == other.worker.name

class Move(Action):
    def __init__(self, direction, worker):
        super().__init__(direction, worker)


class Build(Action):
    def __init__(self, direction, worker):
        super().__init__(direction, worker)
