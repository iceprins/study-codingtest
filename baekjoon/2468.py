import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(g, x, y, n):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            if g[nx][ny] > n and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] += 1

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    height_info = list()
    min_height = 100
    max_height = 1

    for _ in range(N):
        arr = list(map(int, sys.stdin.readline().strip().split()))
        min_height = min(min_height, min(arr))
        max_height = max(max_height, max(arr))
        height_info.append(arr)

    max_height = min(max_height, 100)
    result = list()

    for i in range(min_height - 1, max_height + 1):
        cnt = 0
        visited = [[False for _ in range(N + 1)] for _ in range(N + 1)]
        for j in range(N):
            for k in range(N):
                if height_info[j][k] > i and visited[j][k] == 0:
                    cnt += 1
                    bfs(height_info, j, k, i)
        result.append(cnt)

    print(max(result))