import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(g, x, y):
    queue = deque()
    queue.append((x, y))
    g[x][y] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue
            if g[nx][ny] == 1:
                queue.append((nx, ny))
                g[nx][ny] = 0
                cnt += 1

    return cnt

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().strip().split())
    sketch = list()
    result = list()

    for _ in range(n):
        sketch.append(list(map(int, sys.stdin.readline().strip().split())))

    sketch_cnt = 0
    largest = 0

    for i in range(n):
        for j in range(m):
            if sketch[i][j] == 1:
                largest = max(largest, bfs(sketch, i, j))
                sketch_cnt += 1

    print(sketch_cnt)
    print(largest)