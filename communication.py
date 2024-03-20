def get_board():
    print("podaj plansze: ");
    board = []
    for i in range(9):
        row = input()
        board.append(row)
    return board


def display_board(board):
    for i in range(9):
        print(board[i])

board = get_board();
display_board(board)
