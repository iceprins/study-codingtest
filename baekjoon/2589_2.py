import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    cnt = -sys.maxsize

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > R - 1 or ny < 0 or ny > C - 1 or board[nx][ny] == 'W':
                continue
            if visited[nx][ny] == 0 and board[nx][ny] == 'L':
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                cnt = max(cnt, visited[nx][ny])

    return cnt - 1


if __name__ == '__main__':
    R, C = map(int, sys.stdin.readline().strip().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(R)]
    lands = []

    result = -sys.maxsize

    for i in range(R):
        for j in range(C):
            if board[i][j] == 'L':
                visited = [[0 for _ in range(C)] for _ in range(R)]
                result = max(result, bfs(i, j))

    print(result)
