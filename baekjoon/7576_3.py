import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque()

    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            if box[nx][ny] == 0:
                q.append((nx, ny))
                box[nx][ny] = box[x][y] + 1


if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().strip().split())
    box = []

    for _ in range(N):
        box.append(list(map(int, sys.stdin.readline().strip().split())))

    bfs()

    ans = 0

    for arr in box:
        if 0 in arr:
            ans = 0
            break
        ans = max(ans, max(arr))

    print(ans - 1)
