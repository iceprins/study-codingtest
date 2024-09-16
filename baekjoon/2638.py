import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[0][0] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            if not visited[nx][ny]:
                if board[nx][ny] >= 1:
                    board[nx][ny] += 1
                else:
                    visited[nx][ny] = True
                    q.append((nx, ny))


def removal():
    melted = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] >= 3:
                board[i][j] = 0
                melted += 1
            elif board[i][j] >= 2:
                board[i][j] = 1
    return melted


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

    ans = 0

    while True:
        bfs()
        tmp = removal()

        if tmp:
            ans += 1
        else:
            print(ans)
            break
