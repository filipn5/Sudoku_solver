rows = [[False] * 9] * 9
columns = [[False] * 9] * 9
squares = [[False] * 9] * 9
board = ["0" * 9] * 9

def check(col, row, candidat):
    sqId = (row - 1)*3 + col
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
            if board[i][j] == '0':
                czy = True
                for c in range(1, 9):
                    if check(i, j, c):
                        board[i][j] = str(c)
                        if solve():
                            return True
                        board[i][j] = "0"
    if czy:
        return False
    return True
