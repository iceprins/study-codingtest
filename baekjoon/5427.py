import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while q:
        x, y, c = q.popleft()

        if x == h - 1 or y == w - 1 or x == 0 or y == 0:
            return c

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if building[nx][ny] == '#':
                continue
            if (c + 1 < visited[nx][ny] != -1) or visited[nx][ny] == 0:
                q.append((nx, ny, c + 1))
                visited[nx][ny] = -1

    return 'IMPOSSIBLE'


def fire_spread():
    while fires:
        x, y, t = fires.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if building[nx][ny] == '#' or visited[nx][ny] != 0:
                continue
            visited[nx][ny] = t + 1
            fires.append((nx, ny, t + 1))


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        w, h = map(int, sys.stdin.readline().strip().split())
        building = []
        q = deque()
        fires = deque()
        visited = [[0] * w for _ in range(h)]

        for i in range(h):
            tmp = list(sys.stdin.readline().strip())
            for j in range(w):
                if tmp[j] == '@':
                    q.append((i, j, 1))
                elif tmp[j] == '*':
                    fires.append((i, j, 1))
                    visited[i][j] = 1
            building.append(tmp)

        fire_spread()

        print(bfs())
