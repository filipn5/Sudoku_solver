import communication

size = 10


def check(row, col, candidat):
    sqId = ((row // 3) * 3) + (col // 3)
    if not rows[row][candidat] and not columns[col][candidat] and not squares[sqId][candidat]:
        rows[row][candidat] = True
        columns[col][candidat] = True
        squares[sqId][candidat] = True
        return True
    return False


def solve():
    czy = False
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                czy = True
                for c in range(1, 10):
                    if check(i, j, c):
                        board[i][j] = c
                        if solve():
                            return True
                        board[i][j] = 0
                        rows[i][c] = False
                        columns[j][c] = False
                        squares[(i // 3) * 3 + (j // 3)][c] = False
                if board[i][j] == 0:
                    return False
    if czy:
        return False
    return True


def fillRC():
    for i in range(9):
        for j in range(9):
            rows[i][board[i][j]] = True
            columns[j][board[i][j]] = True
            squares[(i // 3) * 3 + (j // 3)][board[i][j]] = True


def run():
    global board, rows, columns, squares
    board = communication.get_board()
    rows = [[False] * size for _ in range(size)]  # ---
    columns = [[False] * size for _ in range(size)]  # |||
    squares = [[False] * size for _ in range(size)]
    fillRC()
    if solve():
        communication.display_board(board)
    else:
        print("Wrong Board!!!")


if __name__ == '__main__':
    run()
