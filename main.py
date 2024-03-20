import communication
size = 10
rows = [[False] * size] * size #---
columns = [[False] * size] * size #|||
squares = [[False] * size] * size
board = [[]]

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


def fillRC():
    #rows
    for i in range(9):
        for j in range(9):
            rows[i][int(board[i][j])] = True
            columns[j][int(board[i][j])] = True
            squares[(j - 1)*3 + i][int(board[i][j])] = True

def run():
    board = communication.get_board()
    print(int(board[0][6]))
    fillRC()
    solve()
    communication.display_board(board)
if __name__ == '__main__':
    run()
