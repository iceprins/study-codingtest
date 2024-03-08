import sys
from collections import deque

dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    board[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > h - 1 or ny < 0 or ny > w - 1:
                continue
            if board[nx][ny] == 1:
                q.append((nx, ny))
                board[nx][ny] = 0


if __name__ == '__main__':
    while True:
        w, h = map(int, sys.stdin.readline().strip().split())
        board = []

        if w == 0 and h == 0:
            break

        for i in range(h):
            board.append(list(map(int, sys.stdin.readline().strip().split())))

        cnt = 0

        for i in range(h):
            for j in range(w):
                if board[i][j] == 1:
                    bfs(i, j)
                    cnt += 1

        print(cnt)
