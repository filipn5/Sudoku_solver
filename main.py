import communication

size = 10


def check(col, row, candidat):
    sqId = ((row%3) * 3) + (col % 3)
    if rows[row][candidat] == False and columns[col][candidat] == False and squares[sqId][candidat] == False:
        rows[row][candidat] = True
        columns[col][candidat] = True
        squares[sqId][candidat] = True
        return True
    return False


def solve():
    czy = False
    for i in range(9):
        for j in range(9):
            if board[i][j] == "0":
                czy = True
                for c in range(1, 10):
                    if check(i, j, c):
                        print(i,j,c)
                        board[i][j] = str(c)
                        print(board[i][j])
                        if solve():
                            return True
                        board[i][j] = "0"
    if czy:
        return False
    return True


def fillRC():
    for i in range(9):
        for j in range(9):
            rows[i][int(board[i][j])] = True
            columns[j][int(board[i][j])] = True
            squares[((i%3) * 3) + (j % 3)][int(board[i][j])] = True


def run():
    global board, rows, columns, squares
    board = communication.get_board()
    rows = [[False] * size] * size  # ---
    columns = [[False] * size] * size  # |||
    squares = [[False] * size] * size
    fillRC()
    for i in range(9):
        print(rows[i], columns[i], squares[i])
    if solve():
        communication.display_board(board)
    else:
        print("Wrong board")

if __name__ == '__main__':
    run()
