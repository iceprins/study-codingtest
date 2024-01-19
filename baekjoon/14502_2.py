import sys
import copy
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()
    g = copy.deepcopy(lab)

    for i in range(N):
        for j in range(M):
            if g[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            if g[nx][ny] == 0:
                g[nx][ny] = 2
                queue.append((nx, ny))

    global result
    cnt = 0

    for i in range(N):
        cnt += g[i].count(0)

    result = max(result, cnt)


def make_wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                make_wall(cnt + 1)
                lab[i][j] = 0


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    lab = list()

    for _ in range(N):
        lab.append(list(map(int, sys.stdin.readline().strip().split())))

    result = 0
    make_wall(0)

    print(result)
