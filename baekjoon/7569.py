import sys
from collections import deque

graph = list()
queue = deque()
need = 0

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

width, length, height = map(int, sys.stdin.readline().strip().split())

for i in range(height):
    temp = list()
    for j in range(length):
        temp.append(list(map(int, sys.stdin.readline().strip().split())))
        for k in range(width):
            if temp[j][k] == 1:
                queue.append((i, j, k))
    graph.append(temp)


def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or ny < 0 or nz < 0 or nx >= height or ny >= length or nz >= width:
                continue
            if graph[nx][ny][nz] == 0:
                queue.append((nx, ny, nz))
                graph[nx][ny][nz] = graph[x][y][z] + 1


if __name__ == '__main__':
    bfs()
    for i in graph:
        for j in range(length):
            for k in range(width):
                if i[j][k] == 0:
                    print(-1)
                    sys.exit(0)
                need = max(need, max(i[j]))

    print(need - 1)