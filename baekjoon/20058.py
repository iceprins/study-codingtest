import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def rotate(l):
    new_board = [[0] * (2 ** N) for _ in range(2 ** N)]

    for i in range(0, 2 ** N, 2 ** l):
        for j in range(0, 2 ** N, 2 ** l):
            for s in range(2 ** l):
                for t in range(2 ** l):
                    new_board[i + t][2 ** l - 1 + j - s] = board[i + s][j + t]

    return new_board


def decrease():
    target = []
    for i in range(2 ** N):
        for j in range(2 ** N):
            cnt = 0
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if ni < 0 or ni > 2 ** N - 1 or nj < 0 or nj > 2 ** N - 1:
                    continue
                if board[ni][nj] > 0:
                    cnt += 1
            if cnt < 3 and board[i][j] > 0:
                target.append((i, j))

    for x, y in target:
        board[x][y] -= 1


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 0

    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > 2 ** N - 1 or ny < 0 or ny > 2 ** N - 1:
                continue
            if not visited[nx][ny] and board[nx][ny] > 0:
                visited[nx][ny] = True
                q.append((nx, ny))

    return cnt


if __name__ == '__main__':
    N, Q = map(int, sys.stdin.readline().strip().split())
    board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(2 ** N)]
    steps = list(map(int, sys.stdin.readline().strip().split()))
    visited = [[False] * (2 ** N) for _ in range(2 ** N)]

    for i in range(Q):
        if steps[i] != 0:
            board = rotate(steps[i])
        decrease()

    ans_1 = 0
    ans_2 = 0

    for row in board:
        ans_1 += sum(row)

    for i in range(2 ** N):
        for j in range(2 ** N):
            if board[i][j] > 0 and not visited[i][j]:
                ans_2 = max(ans_2, bfs(i, j))

    print(ans_1)
    print(ans_2)
