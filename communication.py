def get_board():
    print("enter the board: ");
    board = []
    for i in range(9):
        row = input()
        lista = []
        for j in range(9):
            lista.append(int(row[j]))
        board.append(lista)
    return board


def display_board(board):
    for i in range(9):
        print(board[i])

