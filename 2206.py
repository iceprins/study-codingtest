import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
board = list()
queue = deque()
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue.append((0, 0, 0))
    while queue:
        x, y, z = queue.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if board[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))
            elif board[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
    return -1


if __name__ == '__main__':
    for _ in range(N):
        board.append(list(map(int, sys.stdin.readline().strip())))

    print(bfs())