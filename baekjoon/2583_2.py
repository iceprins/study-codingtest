import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    board[x][y] += 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > M - 1 or ny < 0 or ny > N - 1:
                continue
            if board[nx][ny] == 0:
                q.append((nx, ny))
                board[nx][ny] += 1
                cnt += 1

    return cnt


if __name__ == '__main__':
    M, N, K = map(int, sys.stdin.readline().strip().split())
    board = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
        for i in range(x1, x2):
            for j in range(y1, y2):
                board[M - 1 - j][i] += 1

    ans = []

    for i in range(M):
        for j in range(N):
            if board[i][j] == 0:
                ans.append(bfs(i, j))

    ans.sort()

    print(len(ans))
    print(*ans)
