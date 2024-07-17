import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        if x == n - 1 and y == n - 1:
            return visited[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
                continue
            if visited[nx][ny] != -1:
                continue
            if board[nx][ny] == 1:
                q.appendleft((nx, ny))
                visited[nx][ny] = visited[x][y]
            else:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    board = []
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[0][0] = 0

    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().strip())))

    print(bfs())
