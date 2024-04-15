import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, direction):
    q = deque()
    q.append((x, y))

    cnt = 0

    while q:
        x, y = q.popleft()
        if room[x][y] == 0:
            room[x][y] = -1
            cnt += 1

        is_blank = False

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            if room[nx][ny] == 0:
                is_blank = True
                break

        if is_blank:
            for _ in range(4):
                direction = (direction + 3) % 4
                if room[x + dx[direction]][y + dy[direction]] == 0:
                    q.append((x + dx[direction], y + dy[direction]))
                    break
            continue

        if room[x - dx[direction]][y - dy[direction]] != 1:
            q.append((x - dx[direction], y - dy[direction]))
            continue
        break

    return cnt


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    r, c, d = map(int, sys.stdin.readline().strip().split())

    room = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

    print(bfs(r, c, d))
