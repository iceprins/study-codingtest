import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
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
            if image[x][y] == image[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    image = []

    for _ in range(N):
        image.append(list(sys.stdin.readline().strip()))

    cnt_normal = 0
    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j)
                cnt_normal += 1

    for i in range(N):
        for j in range(N):
            if image[i][j] == 'G':
                image[i][j] = 'R'

    cnt_blind = 0
    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j)
                cnt_blind += 1

    print(cnt_normal, cnt_blind)
