import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > R - 1 or ny < 0 or ny > C - 1:
                continue
            if (land[nx][ny] == '.' or land[nx][ny] == 'D') and land[x][y] == 'S':
                land[nx][ny] = 'S'
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
            elif (land[nx][ny] == '.' or land[nx][ny] == 'S') and land[x][y] == '*':
                land[nx][ny] = '*'
                q.append((nx, ny))


if __name__ == '__main__':
    R, C = map(int, sys.stdin.readline().strip().split())
    land = [list(sys.stdin.readline().strip()) for _ in range(R)]
    visited = [[-1 for _ in range(C)] for _ in range(R)]
    q = deque()
    Dx, Dy = -1, -1

    for i in range(R):
        for j in range(C):
            if land[i][j] == 'S':
                q.append((i, j))
                visited[i][j] = 0
                break

    for i in range(R):
        for j in range(C):
            if land[i][j] == '*':
                q.append((i, j))

    for i in range(R):
        for j in range(C):
            if land[i][j] == 'D':
                Dx, Dy = i, j

    bfs()

    if visited[Dx][Dy] != -1:
        print(visited[Dx][Dy])
    else:
        print("KAKTUS")
