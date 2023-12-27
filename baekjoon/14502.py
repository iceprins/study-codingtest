import copy
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()
    b = copy.deepcopy(board)
    for i in range(N):
        for j in range(M):
            if b[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if b[nx][ny] == 0:
                    b[nx][ny] = 2
                    queue.append((nx, ny))
    global ans
    temp = 0
    for i in range(N):
        for j in range(M):
            if b[i][j] == 0:
                temp += 1

    ans = max(ans, temp)


def make_wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                make_wall(cnt + 1)
                board[i][j] = 0


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

    ans = 0
    make_wall(0)
    print(ans)