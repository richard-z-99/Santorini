from santorini_classes import*

class Board:
    def __init__(self, kind1, kind2, color):
        self.player_factory = PlayerFactory()
        self.white_player = self.player_factory.create_player(kind1, "white")
        self.blue_player = self.player_factory.create_player(kind2, "blue")
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


    def get_legal_moves(self, player):
        workers = [player.worker1, player.worker2]
        legal_moves = []

        for d in directions.keys():
            for w in workers:
                move = Move(d, w)
                if self.check_move(move):
                    legal_moves.append(move)

        return legal_moves


    def get_legal_builds(self, player):
        workers = [player.worker1, player.worker2]
        legal_moves = []
        
        for d in directions.keys():
            for w in workers:
                build = Build(d, w)
                if self.check_build(build):
                    legal_moves.append(build)

        return legal_moves



    #returns true if action stays on board, new square is unoccupied, and not moving to level 4 square.
    def check_board(self, action):
        #self.update_board()
        new_row = action.get_new_coords()[0]
        new_col = action.get_new_coords()[1]

        if (0 <= new_row < 5 and 0 <= new_col < 5):
            occupant = self.get_square(new_row, new_col).occupant
            level = self.get_square(new_row, new_col).level
            
            if (occupant is None and level < 4):
                return True
            else:
                #print("Cannot move {}".format(action.direction))
                return False
        else:
            #print("Cannot move {}".format(action.direction))
            return False



    #returns true if action stays on board, new square is unoccupied, and not building on level 4 square.
    def check_build(self, build):
        if(not self.check_board(build)):
            return False



    #checks if move is valid
    def check_move(self, move):
        #self.update_board()
        if(not self.check_board(move)):
            return False

        new_row = move.get_new_coords()[0]
        new_col = move.get_new_coords()[1]
        old_row = move.worker.row
        old_col = move.worker.col
        
        old_level = self.get_square(old_row, old_col).level
        new_level = self.get_square(new_row, new_col).level
        return (new_level < 4 and new_level-old_level <= 1)


    def check_won(self, player):
        level1 = self.get_square(player.worker1.row, player.worker1.col).level
        level2 = self.get_square(player.worker2.row, player.worker2.col).level
        return (level1 == 3 or level2 == 3)




    #calculate distance between two squares
    def square_dist(self, square1, square2):
        row_dist = abs(square1.row - square2.row)
        col_dist = abs(square1.col - square2.col)
        return min(row_dist, col_dist) + abs(row_dist - col_dist)


    #calculate distance between two workers
    def worker_dist(self, worker1, worker2):
        square1 = self.get_square(worker1.row, worker1.col)
        square2 = self.get_square(worker2.row, worker2.col)
        return self.square_dist(square1, square2)


    #calculate height score of player in given position
    def height_score(self, player):
        level1 = self.get_square(player.worker1.row, player.worker1.col).level
        level2 = self.get_square(player.worker2.row, player.worker2.col).level
        return level1 + level2


    #calculate center score of player in given position
    def center_score(self, player):
        center_square = self.get_square(2,2)
        square1 = self.get_square(player.worker1.row, player.worker1.col)
        square2 = self.get_square(player.worker2.row, player.worker2.col)

        d1 = self.square_dist(square1, center_square)
        d2 = self.square_dist(square2, center_square)

        d1 = max(2-d1, 0)
        d2 = max(2-d2, 0)

        return d1+d2


    #calculate the distance score of player in given position
    def distance_score(self, player):
        opponent = self.get_opponent(player)

        #dij = distance from player.workeri to opponent.workerj
        d11 = self.worker_dist(player.worker1, opponent.worker1)
        d21 = self.worker_dist(player.worker2, opponent.worker1)
        d12 = self.worker_dist(player.worker1, opponent.worker2)
        d22 = self.worker_dist(player.worker2, opponent.worker2)

        return 9 - (min(d11, d21) + min(d12, d22))


    def score(self, player):
        c1, c2, c3 = 3, 2, 1
        return c1*self.height_score(player) + c2*self.center_score(player) + c3*self.distance_score(player)


    def execute_move(self, move):
        old_row = move.worker.row
        old_col = move.worker.col
        new_row = move.get_new_coords()[0]
        new_col = move.get_new_coords()[1]

        move.worker.update_location(new_row, new_col)

        #update occupancy status of old/new squares
        old_square = self.get_square(old_row, old_col)
        old_square.update_occupant(None)

        new_square = self.get_square(new_row, new_col)
        new_square.update_occupant(move.worker)


    def execute_build(self, build):
        new_row = build.get_new_coords()[0]
        new_col = build.get_new_coords()[1]

        #update level of new_square
        new_square = self.board.get_square(new_row, new_col)
        new_square.update_level()
        


    #returns the opponent of the input player
    def get_opponent(self, player):
        if(player == self.white_player):
            return self.blue_player
        elif(player == self.blue_player):
            return self.white_player
        else:
            print("Invalid player!")


    def switch_player(self):
        self.curr_player = self.get_opponent(self.curr_player)


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
