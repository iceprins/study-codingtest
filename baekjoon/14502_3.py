import copy
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque()
    graph = copy.deepcopy(lab_map)

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx, ny))

    global ans
    cnt = 0

    for i in range(N):
        cnt += graph[i].count(0)

    ans = max(ans, cnt)


def make_wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if lab_map[i][j] == 0:
                lab_map[i][j] = 1
                make_wall(cnt + 1)
                lab_map[i][j] = 0


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    lab_map = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

    ans = 0
    make_wall(0)

    print(ans)
