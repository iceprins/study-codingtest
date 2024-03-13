import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            if earth[nx][ny] == 0:
                visited[x][y] += 1
            if visited[nx][ny] == 0 and earth[nx][ny] != 0:
                q.append((nx, ny))
                visited[nx][ny] += 1


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    earth = []

    for _ in range(N):
        earth.append(list(map(int, sys.stdin.readline().strip().split())))

    ans = 0

    while True:
        cnt = 0
        visited = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if not visited[i][j] and earth[i][j] != 0:
                    bfs(i, j)
                    cnt += 1

        for i in range(N):
            for j in range(M):
                if visited[i][j] != 0:
                    earth[i][j] -= (visited[i][j] - 1)
                    if earth[i][j] < 0:
                        earth[i][j] = 0

        ans += 1
        if cnt == 0:
            ans = 1
            break
        if cnt >= 2:
            break

    print(ans - 1)
