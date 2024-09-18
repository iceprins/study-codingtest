import sys


def is_promise(x, y, n):
    for i in range(9):
        if board[x][i] == n:
            return False

    for i in range(9):
        if board[i][y] == n:
            return False

    for i in range(x - x % 3, x - x % 3 + 3):
        for j in range(y - y % 3, y - y % 3 + 3):
            if board[i][j] == n:
                return False

    return True


def dfs(idx):
    global flag

    if flag:
        return

    if idx >= len(cand):
        flag = True
        for i in range(9):
            print(''.join(map(str, board[i])))
        return

    x, y = cand[idx]

    for i in range(1, 10):
        if is_promise(x, y, i):
            board[x][y] = i
            dfs(idx + 1)
            board[x][y] = 0


if __name__ == '__main__':
    board = [list(map(int, sys.stdin.readline().strip())) for _ in range(9)]
    cand = []
    flag = False

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                cand.append((i, j))

    dfs(0)
