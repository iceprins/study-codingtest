import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, v):
    global count
    queue = deque()
    queue.append((x, y))
    v[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            if iceberg[nx][ny] == 0:
                count[x][y] += 1
                continue
            if not v[nx][ny] and iceberg[nx][ny] != 0:
                queue.append((nx, ny))
                v[nx][ny] = True

    return 1


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    iceberg = list()

    for _ in range(N):
        iceberg.append(list(map(int, sys.stdin.readline().strip().split())))

    cnt = 0
    year = 0

    while True:
        count = [[0 for _ in range(M)] for _ in range(N)]
        visited = [[False for _ in range(M)] for _ in range(N)]
        result = list()

        for i in range(N):
            for j in range(M):
                if iceberg[i][j] != 0 and not visited[i][j]:
                    result.append(bfs(i, j, visited))

        for i in range(N):
            for j in range(M):
                iceberg[i][j] = max(0, iceberg[i][j] - count[i][j])

        if len(result) == 0:
            print(0)
            break
        if len(result) >= 2:
            print(year)
            break

        year += 1
