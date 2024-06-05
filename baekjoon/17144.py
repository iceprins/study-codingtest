import sys


def spread():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    tmp = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if room[i][j] != 0 and room[i][j] != -1:
                amount = room[i][j] // 5
                cnt = 0
                for k in range(4):
                    if i + dx[k] < 0 or i + dx[k] > R - 1 or j + dy[k] < 0 or j + dy[k] > C - 1:
                        continue
                    if room[i + dx[k]][j + dy[k]] != -1:
                        cnt += 1
                        tmp[i + dx[k]][j + dy[k]] += amount
                tmp[i][j] -= amount * cnt

    for i in range(R):
        for j in range(C):
            room[i][j] += tmp[i][j]


def purify_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    idx = 0
    before = 0
    up_x, up_y = purifier[0]
    x, y = up_x, up_y + 1

    while True:
        nx = x + dx[idx]
        ny = y + dy[idx]

        if x == up_x and y == 0:
            break

        if nx < 0 or nx > R - 1 or ny < 0 or ny > C - 1:
            idx += 1
            continue

        room[x][y], before = before, room[x][y]

        x = nx
        y = ny


def purify_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    idx = 0
    before = 0
    down_x, down_y = purifier[1]
    x, y = down_x, down_y + 1

    while True:
        nx = x + dx[idx]
        ny = y + dy[idx]

        if x == down_x and y == 0:
            break

        if nx < 0 or nx > R - 1 or ny < 0 or ny > C - 1:
            idx += 1
            continue

        room[x][y], before = before, room[x][y]

        x = nx
        y = ny


if __name__ == '__main__':
    R, C, T = map(int, sys.stdin.readline().strip().split())
    room = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(R)]
    purifier = []

    for i in range(R):
        for j in range(C):
            if room[i][j] == -1:
                purifier.append((i, j))

    for _ in range(T):
        spread()
        purify_up()
        purify_down()

    ans = 0

    for row in room:
        ans += sum(row)
    ans += 2

    print(ans)
