import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    union = []
    union.append((x, y))

    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny] == 1:
                continue
            if L <= abs(land[now_x][now_y] - land[nx][ny]) <= R:
                visited[nx][ny] = 1
                q.append((nx, ny))
                union.append((nx, ny))

    return union


if __name__ == '__main__':
    N, L, R = map(int, sys.stdin.readline().strip().split())
    land = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

    ans = 0

    while True:
        flag = 0
        visited = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0:
                    visited[i][j] = 1
                    country = bfs(i, j)

                    if len(country) > 1:
                        flag = 1
                        result = sum(land[a][b] for a, b in country) // len(country)

                        for a, b in country:
                            land[a][b] = result

        if flag == 0:
            print(ans)
            break
        ans += 1
