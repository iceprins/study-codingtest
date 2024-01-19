import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(g, x, y):
    global visited
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            if g[nx][ny] == g[x][y] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    painting = list()

    for _ in range(N):
        painting.append(list(sys.stdin.readline().strip()))

    visited = [[0 for _ in range(N)] for _ in range(N)]

    ans_normal = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                bfs(painting, i, j)
                ans_normal += 1

    print(visited)

    for i in range(N):
        for j in range(N):
            if painting[i][j] == 'G':
                painting[i][j] = 'R'

    visited = [[0 for _ in range(N)] for _ in range(N)]

    ans_blind = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                bfs(painting, i, j)
                ans_blind += 1

    print(ans_normal, ans_blind)
