import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(g, x, y):
    queue = deque()
    queue.append((x, y))
    g[x][y] = 0
    result = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if g[nx][ny] != 0:
                queue.append((nx, ny))
                g[nx][ny] = 0
                result += 1

    return result

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    complex_map = list()
    complex_info = list()

    for _ in range(N):
        complex_map.append(list(map(int, sys.stdin.readline().strip())))

    for i in range(N):
        for j in range(N):
            if complex_map[i][j] != 0:
                complex_info.append(bfs(complex_map, i, j))

    complex_info.sort()

    print(len(complex_info))
    for elem in complex_info:
        print(elem)