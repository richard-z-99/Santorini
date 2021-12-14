from main import PlayGame, Memento
from santorini_classes import Move, Build, Worker, Board

game = PlayGame()
board = game.memento.history[0]
a = board.white_player.worker1
#print("{}, {}".format(a.row, a.col))
move1 = Move('n', a)
build1 = Build('n', a)
build2 = Build('w', a)

print("----------Starting----------")
game.print_curr_board()
game.execute_move(move1)

print("move 1:")
game.print_curr_board()

if(game.check_build(build1)):
    game.execute_build(build1)
else:
    print("boo!")
    game.execute_build(build2)

print("build 1:")
game.print_curr_board()

game.undo()
print("after undo:")
game.print_curr_board()

game.redo()
print("after redo:")
game.print_curr_board()






