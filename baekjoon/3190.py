import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def game():
    q = deque()
    q.append((0, 0))
    nx, ny = 0, 0
    dir_idx = 0
    cnt = 0

    while True:
        nx += dx[dir_idx]
        ny += dy[dir_idx]
        cnt += 1

        if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1 or (nx, ny) in q:
            break

        q.append((nx, ny))

        if board[nx][ny] == 0:
            q.popleft()
        elif board[nx][ny] == 1:
            board[nx][ny] = 0

        if direction and direction[0][0] == cnt:
            sec, alpha = direction.popleft()
            if alpha == 'L':
                dir_idx = (dir_idx - 1) % 4
            else:
                dir_idx = (dir_idx + 1) % 4

    return cnt


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    K = int(sys.stdin.readline().strip())

    board = [[0 for _ in range(N)] for _ in range(N)]

    for _ in range(K):
        a, b = map(int, sys.stdin.readline().strip().split())
        board[a - 1][b - 1] = 1

    L = int(sys.stdin.readline().strip())

    direction = deque()

    for _ in range(L):
        a, b = sys.stdin.readline().strip().split()
        direction.append((int(a), b))

    print(game())
