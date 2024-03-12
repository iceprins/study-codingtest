import sys
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(x, y):
    if x == x2 and y == y2:
        return 0
    q = deque()
    q.append((x, y))
    board[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > I - 1 or ny < 0 or ny > I - 1:
                continue
            if nx == x2 and ny == y2:
                return board[x][y]
            if board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        I = int(sys.stdin.readline().strip())
        board = [[0 for _ in range(I)] for _ in range(I)]
        x1, y1 = map(int, sys.stdin.readline().strip().split())
        x2, y2 = map(int, sys.stdin.readline().strip().split())

        print(bfs(x1, y1))
