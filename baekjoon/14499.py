import sys

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def move(direction):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    if direction == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif direction == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif direction == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b


if __name__ == '__main__':
    N, M, x, y, K = map(int, sys.stdin.readline().strip().split())
    board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    order = list(map(int, sys.stdin.readline().strip().split()))

    dice = [0, 0, 0, 0, 0, 0]

    nx, ny = x, y

    for i in order:
        nx += dx[i - 1]
        ny += dy[i - 1]

        if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
            nx -= dx[i - 1]
            ny -= dy[i - 1]
            continue

        move(i)

        if board[nx][ny] == 0:
            board[nx][ny] = dice[-1]
        else:
            dice[-1] = board[nx][ny]
            board[nx][ny] = 0

        print(dice[0])
