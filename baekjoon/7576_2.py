import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(g):
    queue = deque()

    for i in range(N):
        for j in range(M):
            if g[i][j] == 1:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            if g[nx][ny] == 0:
                g[nx][ny] = g[x][y] + 1
                queue.append((nx, ny))

def solve():
    ans = 0
    for row in range(N):
        if 0 in box[row]:
            return -1
        ans = max(ans, max(box[row]))

    return ans - 1


if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().strip().split())
    box = list()

    for _ in range(N):
        box.append(list(map(int, sys.stdin.readline().strip().split())))

    bfs(box)

    print(solve())