import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, h):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            if not visited[nx][ny] and info[nx][ny] > h:
                q.append((nx, ny))
                visited[nx][ny] = True


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    info = []
    height_max = 1
    ans = 0

    for _ in range(N):
        arr = list(map(int, sys.stdin.readline().strip().split()))
        height_max = max(height_max, max(arr))
        info.append(arr)

    for i in range(height_max):
        visited = [[False for _ in range(N)] for _ in range(N)]
        cnt = 0

        for j in range(N):
            for k in range(N):
                if visited[j][k] == False and info[j][k] > i:
                    bfs(j, k, i)
                    cnt += 1

        ans = max(ans, cnt)

    print(ans)
