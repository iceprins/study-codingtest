import sys
from collections import deque


n, m = map(int, sys.stdin.readline().strip().split())
board = list()
visited = [[-1] * m for _ in range(n)]
queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split())))


def bfs(x, y):
    queue.append((x, y))
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if board[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif board[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


if __name__ == '__main__':
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2 and visited[i][j] == -1:
                bfs(i, j)

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                print(0, end=' ')
            else:
                print(visited[i][j], end=' ')
        print()