import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    board[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            if board[nx][ny] != 0:
                q.append((nx, ny))
                board[nx][ny] = 0


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        M, N, K = map(int, sys.stdin.readline().strip().split())
        board = [[0 for _ in range(M)] for _ in range(N)]

        for i in range(K):
            a, b = map(int, sys.stdin.readline().strip().split())
            board[b][a] = 1

        cnt = 0

        for i in range(N):
            for j in range(M):
                if board[i][j] == 1:
                    bfs(i, j)
                    cnt += 1

        print(cnt)
