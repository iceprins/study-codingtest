import sys
from collections import deque


N, M, T = map(int, sys.stdin.readline().strip().split())
board = list()
queue = deque()
queue.append((0, 0))
visited = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().strip().split())))


def bfs():
    gram = 10001
    queue.append((0, 0))
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()
        if (x, y) == (N - 1, M - 1):
            return min(visited[x][y] - 1, gram)
        if board[x][y] == 2:
            gram = visited[x][y] - 1 + N - 1 - x + M - 1 - y

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if board[nx][ny] == 0 or board[nx][ny] == 2:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    return gram


if __name__ == '__main__':
    result = bfs()
    if result <= T:
        print(result)
    else:
        print("Fail")