import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] += 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > rows - 1 or ny < 0 or ny > columns - 1:
                continue
            if treasure_map[nx][ny] == 'W':
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                cnt = max(cnt, visited[nx][ny])
                q.append((nx, ny))

    return cnt


if __name__ == '__main__':
    rows, columns = map(int, sys.stdin.readline().strip().split())
    treasure_map = list()

    for _ in range(rows):
        treasure_map.append(list(sys.stdin.readline().strip()))

    ans = -sys.maxsize

    for i in range(rows):
        for j in range(columns):
            if treasure_map[i][j] == 'L':
                visited = [[0 for _ in range(columns)] for _ in range(rows)]
                bfs(i, j)
                for k in visited:
                    ans = max(ans, max(k))

    print(ans - 1)
