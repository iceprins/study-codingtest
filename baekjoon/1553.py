import sys

dx = [1, 0]
dy = [0, 1]


def solve(x, y):
    if x == 8:
        return 1
    cnt = 0
    nx, ny = x, y + 1
    if ny == 7:
        nx, ny = x + 1, 0
    if visited[x][y]:
        return solve(nx, ny)

    now = board[x][y]
    visited[x][y] = True
    for i in range(2):
        mx = x + dx[i]
        my = y + dy[i]
        if mx < 0 or mx > 7 or my < 0 or my > 6:
            continue
        pair = board[mx][my]
        if not visited[mx][my] and not domino[now][pair]:
            domino[now][pair] = domino[pair][now] = True
            visited[mx][my] = True
            cnt += solve(nx, ny)
            visited[mx][my] = False
            domino[now][pair] = domino[pair][now] = False

    visited[x][y] = False

    return cnt


if __name__ == '__main__':
    board = [list(map(int, sys.stdin.readline().strip())) for _ in range(8)]
    visited = [[False] * 7 for _ in range(8)]
    domino = [[False] * 7 for _ in range(7)]

    print(solve(0, 0))
