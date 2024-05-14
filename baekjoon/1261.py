import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            if visited[nx][ny] == -1:
                if maze[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx, ny))
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))


if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().strip().split())
    maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    visited = [[-1 for _ in range(M)] for _ in range(N)]

    bfs()

    print(visited[N - 1][M - 1])
