import numpy as np

# game board
board = np.zeros((3,3), dtype=int)

def print_board():
    for row in board:
        print('|'.join(['X' if cell == 1 else 'O' if cell == -1 else ' ' for cell in row]))
        print('-'*5)

def check_winner():
    rows_sum = np.sum(board, axis=1)
    cols_sum =  np.sum(board, axis=0)
    diagonal_sum1= np.trace(board)
    diagonal_sum2= np.trace(np.fliplr(board))

    sums = np.concatenate((rows_sum,cols_sum, [diagonal_sum1, diagonal_sum2]))

    if any(abs(s) == 3 for s in sums):
        return True
    return False

def  make_move(row, col,player):
    if row<0 or row>=3 or col<0 or col>=3 or board[row][col] !=0:
        print("Invalid move! Try Again")
        return False
    
    board[row][col] = player
    return True

# Start the game
current_player=1

while True:
    print_board()
    if current_player == -1:
        the_current_player = current_player + 3
    else:
        the_current_player = current_player
    print(f"Player {the_current_player}'s turn")

    row = int(input(" enter the row (0-2): "))
    col = int(input(" enter the col (0-2): "))

    if make_move(row, col, current_player):
        if check_winner():
            print_board()
            if current_player == -1:
                the_current_player = current_player + 3
            else:
                the_current_player = current_player
            print(f"Player {the_current_player} wins")
            break

        if 0 not in board:
            print_board()
            print("Tie")
            break

    current_player = -1 if current_player == 1 else 1

