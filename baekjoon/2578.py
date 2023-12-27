import sys

board = list()
host = list()

for _ in range(5):
    board.append(list(map(int, sys.stdin.readline().strip().split())))

for _ in range(5):
    host += sys.stdin.readline().strip().split()


def is_bingo():
    result = 0

    for row in board:
        if row.count(0) == 5:
            result += 1

    for i in range(5):
        c_column = 0
        for j in range(5):
            if board[j][i] == 0:
                c_column += 1
        if c_column == 5:
            result += 1

    c_left = 0
    for i in range(5):
        if board[i][i] == 0:
            c_left += 1
        if c_left == 5:
            result += 1

    c_right = 0
    for i in range(5):
        if board[i][4-i] == 0:
            c_right += 1
        if c_right == 5:
            result += 1

    return result


if __name__ == '__main__':

    for k in range(25):
        temp = [(i, j) for i in range(5) for j in range(5) if board[i][j] == int(host[k])]
        board[temp[0][0]][temp[0][1]] = 0

        if is_bingo() >= 3:
            print(k+1)
            break