import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def get_dist(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[x][y] = 1
    cand = []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            if visited[nx][ny] == 0:
                if shark_size > space[nx][ny] != 0:
                    visited[nx][ny] = visited[x][y] + 1
                    cand.append((visited[nx][ny] - 1, nx, ny))
                elif shark_size == space[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                elif space[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    return sorted(cand, key=lambda x: (x[0], x[1], x[2]))


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    space = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    fish = []

    sx, sy = -1, -1
    shark_size = 2

    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:
                sx, sy = i, j
                space[i][j] = 0

    cnt, eat = 0, 0

    while True:
        fish = deque(get_dist(sx, sy))

        if not fish:
            break

        target_dist, target_x, target_y = fish.popleft()

        cnt += target_dist
        eat += 1
        space[target_x][target_y] = 0

        if eat == shark_size:
            shark_size += 1
            eat = 0

        sx, sy = target_x, target_y

    print(cnt)
