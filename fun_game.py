import numpy as np
def board():
    board = np.zeros((6, 7))
    return board

board = board()
print(board)
turn = 0

game_over = False
while not game_over:
    #Player 1 Input
    if turn == 0:
        selectionPlay1 = input("Player 1 Drop Position (0-6)>> ")

    #Player 2 Input