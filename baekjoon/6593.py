import sys
from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    while q:
        x, y, z = q.popleft()
        if x == exit_x and y == exit_y and z == exit_z:
            return visited[x][y][z]
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx > L - 1 or ny < 0 or ny > R - 1 or nz < 0 or nz > C - 1:
                continue
            if building[nx][ny][nz] == '#':
                continue
            if visited[nx][ny][nz] == 0:
                visited[nx][ny][nz] = visited[x][y][z] + 1
                q.append((nx, ny, nz))

    return -1


if __name__ == '__main__':
    while True:
        L, R, C = map(int, sys.stdin.readline().strip().split())

        if L == 0 and R == 0 and C == 0:
            break

        building = []
        visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]

        for _ in range(L):
            tmp = [list(sys.stdin.readline().strip()) for _ in range(R)]
            building.append(tmp)

            sys.stdin.readline().strip()

        q = deque()
        exit_x, exit_y, exit_z = -1, -1, -1

        for i in range(L):
            for j in range(R):
                for k in range(C):
                    if building[i][j][k] == 'S':
                        q.append((i, j, k))
                    if building[i][j][k] == 'E':
                        exit_x, exit_y, exit_z = i, j, k

        result = bfs()

        if result == -1:
            print("Trapped!")
        else:
            print(f"Escaped in {result} minute(s).")
