import numpy as np
def board():
    board = np.zeros((6, 7))
    return board

board = board()
print(board)
turn = 0
rowCount = 6
colCount = 7
def piece_drop(board, row, col, piece):
    board[row][col] = piece
def valLocation(board, col):
    return board[5][col]==0
def get_next_open_row(board, col):
	for row in reversed(range(rowCount)):
		if board[row][col] == 0:
			return row
game_over = False
while not game_over:
    #Players 1 Input
    if turn == 0:
        col = int(input("Player 1 Drop Row (0-6)>> "))
        if valLocation(board, col):
            row = get_next_open_row(board, col)
            piece_drop(board, row, col, 1)
        print(board)

    else:
        col = int(input("Player 2 Drop Row (0-6)>> "))
        if valLocation(board, col):
            row = get_next_open_row(board, col)
            piece_drop(board, row, col, 1)
        print(board)

    turn +=1
    turn %= 2

