#TODO naprwaic solve - ranodmow wstawia true w rowsach
import communication

size = 10


def check(row, col, candidat):
    sqId = ((row//3) * 3) + (col // 3)
    if not rows[row][candidat] and not columns[col][candidat] and not squares[sqId][candidat]:
        rows[row][candidat] = True
        columns[col][candidat] = True
        squares[sqId][candidat] = True
        return True
    return False


def solve():
    communication.display_board(board)
    print()
    czy = False
    for i in range(9):
        for j in range(9):
            if(i == 0 and j == 3):
                print(rows[i], columns[j])
                print(check(i,j, 9))
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
                        squares[(i //3)*3 + (j // 3)][c] = False
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
            squares[(i //3)*3 + (j // 3)][board[i][j]] = True


def run():
    global board, rows, columns, squares
    board = communication.get_board()
    rows = [[False] * size for _ in range(size)]  # ---
    columns = [[False] * size for _ in range(size)] # |||
    squares = [[False] * size for _ in range(size)]
    fillRC()
    print(rows[0])
    czy = solve()
    print("zostalo")
    communication.display_board(board)
    print(czy)

if __name__ == '__main__':
    run()
