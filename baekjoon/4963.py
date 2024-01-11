import sys
from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(g, x, y):
    queue = deque()
    queue.append((x, y))
    g[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > h - 1 or ny < 0 or ny > w - 1:
                continue
            if g[nx][ny] == 1:
                queue.append((nx, ny))
                g[nx][ny] = 0


if __name__ == '__main__':
    while True:
        w, h = map(int, sys.stdin.readline().strip().split())
        graph = list()

        if w == 0 and h == 0:
            break

        for _ in range(h):
            graph.append(list(map(int, sys.stdin.readline().strip().split())))

        cnt = 0

        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    bfs(graph, i, j)
                    cnt += 1

        print(cnt)