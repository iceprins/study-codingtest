import math
import sys

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def move(x, y):
    d = 0
    space = 1
    for _ in range(N - 1):
        for _ in range(2):
            for _ in range(space):
                nx = x + dx[d]
                ny = y + dy[d]
                sand(nx, ny, d)
                x, y = nx, ny
            d = (d + 1) % 4
        space += 1

    for _ in range(N - 1):
        nx = x + dx[d]
        ny = y + dy[d]
        sand(nx, ny, d)
        x, y = nx, ny


def sand(x, y, d):
    global ans
    one_percent = [[(-1, 1), (1, 1)], [(-1, -1), (-1, 1)], [(-1, -1), (1, -1)], [(1, -1), (1, 1)]]
    two_percent = [[(-2, 0), (2, 0)], [(0, -2), (0, 2)]]
    five_percent = [[(0, -2)], [(2, 0)], [(0, 2)], [(-2, 0)]]
    seven_percent = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]]
    ten_percent = [[(-1, -1), (1, -1)], [(1, -1), (1, 1)], [(-1, 1), (1, 1)], [(-1, -1), (-1, 1)]]
    rest = [[(0, - 1)], [(1, 0)], [(0, 1)], [(-1, 0)]]

    tmp = 0

    for dx, dy in one_percent[d]:
        nx = x + dx
        ny = y + dy
        if not (nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1):
            board[nx][ny] += math.floor((board[x][y]) * 0.01)
        else:
            ans += math.floor((board[x][y]) * 0.01)
        tmp += math.floor((board[x][y]) * 0.01)

    for dx, dy in two_percent[d % 2]:
        nx = x + dx
        ny = y + dy
        if not (nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1):
            board[nx][ny] += math.floor((board[x][y]) * 0.02)
        else:
            ans += math.floor((board[x][y]) * 0.02)
        tmp += math.floor((board[x][y]) * 0.02)

    for dx, dy in five_percent[d]:
        nx = x + dx
        ny = y + dy
        if not (nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1):
            board[nx][ny] += math.floor((board[x][y]) * 0.05)
        else:
            ans += math.floor((board[x][y]) * 0.05)
        tmp += math.floor((board[x][y]) * 0.05)

    for dx, dy in seven_percent[d % 2]:
        nx = x + dx
        ny = y + dy
        if not (nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1):
            board[nx][ny] += math.floor((board[x][y]) * 0.07)
        else:
            ans += math.floor((board[x][y]) * 0.07)
        tmp += math.floor((board[x][y]) * 0.07)

    for dx, dy in ten_percent[d]:
        nx = x + dx
        ny = y + dy
        if not (nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1):
            board[nx][ny] += math.floor((board[x][y]) * 0.1)
        else:
            ans += math.floor((board[x][y]) * 0.1)
        tmp += math.floor((board[x][y]) * 0.1)

    for dx, dy in rest[d]:
        nx = x + dx
        ny = y + dy
        if not (nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1):
            board[nx][ny] += (board[x][y] - tmp)
        else:
            ans += (board[x][y] - tmp)

    board[x][y] = 0


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

    ans = 0
    sx, sy = N // 2, N // 2

    move(sx, sy)

    print(ans)
