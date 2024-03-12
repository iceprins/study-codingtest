import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    paper[x][y] = 0
    ans = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue
            if paper[nx][ny] != 0:
                q.append((nx, ny))
                paper[nx][ny] = 0
                ans += 1

    return ans


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().strip().split())
    paper = []

    for _ in range(n):
        paper.append(list(map(int, sys.stdin.readline().strip().split())))

    cnt = 0
    area = [0]

    for i in range(n):
        for j in range(m):
            if paper[i][j] != 0:
                area.append(bfs(i, j))
                cnt += 1

    print(cnt)
    print(max(area))
