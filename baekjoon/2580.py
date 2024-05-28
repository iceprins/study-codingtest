import sys


def is_promise(x, y, target):
    for i in range(9):
        if board[x][i] == target:
            return False

    for i in range(9):
        if board[i][y] == target:
            return False

    for i in range(x - x % 3, x - x % 3 + 3):
        for j in range(y - y % 3, y - y % 3 + 3):
            if board[i][j] == target:
                return False

    return True


def solve(depth):
    if depth == len(q):
        for row in board:
            print(*row)
        exit()

    x, y = q[depth][0], q[depth][1]
    for i in range(1, 10):
        if is_promise(x, y, i):
            board[x][y] = i
            solve(depth + 1)
            board[x][y] = 0


if __name__ == '__main__':
    board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]
    q = []

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                q.append((i, j))

    solve(0)
