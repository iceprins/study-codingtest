import sys
from collections import deque


W, H = map(int, sys.stdin.readline().strip().split())
board = [[0 for _ in range(W + 2)] for _ in range(H + 2)]
visited = [[False for _ in range(W + 2)] for _ in range(H + 2)]
queue = deque()

for i in range(1, H + 1):
    board[i][1:W + 1] = map(int, sys.stdin.readline().strip().split())

dx = [0, 1, 1, 0, -1, -1]
dy_o = [1, 1, 0, -1, 0, 1]
dy_e = [1, 0, -1, -1, -1, 0]


def bfs():
    wall_len = 0
    queue.append((0, 0))
    # visited = [[False for _ in range(W + 2)] for _ in range(H + 2)]
    visited[0][0] = True
    while queue:
        x, y = queue.popleft()
        for i in range(6):
            if x % 2 == 0:
                ny = y + dy_e[i]
            else:
                ny = y + dy_o[i]
            nx = x + dx[i]
            if 0 <= ny < W + 2 and 0 <= nx < H + 2:
                if board[nx][ny] == 0 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                elif board[nx][ny] == 1:
                    wall_len += 1

    return wall_len


if __name__ == '__main__':
    print(bfs())