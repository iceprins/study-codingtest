import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            if not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                board[nx][ny] = num
                q.append((nx, ny))


def find(v):
    q = deque()
    dist = [[-1] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == v:
                dist[i][j] = 0
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            if board[nx][ny] != 0 and board[nx][ny] != v:
                return dist[x][y]
            if board[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    return sys.maxsize


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    num = 1
    ans = sys.maxsize

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                board[i][j] = num
                bfs(i, j)
                num += 1

    for i in range(1, num):
        ans = min(ans, find(i))

    print(ans)
