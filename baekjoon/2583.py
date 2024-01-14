import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(g, x, y):
    queue = deque()
    queue.append((x, y))
    g[x][y] += 1
    area = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > M - 1 or ny < 0 or ny > N - 1:
                continue
            if g[nx][ny] == 0:
                queue.append((nx, ny))
                g[nx][ny] += 1
                area += 1

    return area


if __name__ == '__main__':
    M, N, K = map(int, sys.stdin.readline().strip().split())
    paper = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
        for i in range(x1, x2):
            for j in range(y1, y2):
                paper[j][i] += 1

    cnt = 0
    areas = list()

    for i in range(M):
        for j in range(N):
            if paper[i][j] == 0:
                areas.append(bfs(paper, i, j))
                cnt += 1

    areas.sort()

    print(cnt)
    print(*areas)
