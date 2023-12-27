import sys
from collections import deque

width, depth = map(int, sys.stdin.readline().strip().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = list()
queue = deque()
need = 0

for _ in range(depth):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(depth):
    for j in range(width):
        if graph[i][j] == 1:
            queue.append((i, j))


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= depth or ny >= width:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


if __name__ == '__main__':
    bfs()
    for i in range(depth):
        if 0 in graph[i]:
            print(-1)
            sys.exit(0)
        need = max(need, max(graph[i]))
    print(need - 1)