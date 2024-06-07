import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def increase():
    n = len(q)
    for _ in range(n):
        num, x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            if tube[nx][ny] != 0:
                continue
            tube[nx][ny] = num
            q.append((num, nx, ny))


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().strip().split())
    tube = []
    q = []

    for i in range(N):
        tmp = list(map(int, sys.stdin.readline().strip().split()))
        for j in range(N):
            if tmp[j] != 0:
                q.append((tmp[j], i, j))
        tube.append(tmp)

    S, X, Y = map(int, sys.stdin.readline().strip().split())

    q.sort()
    q = deque(q)

    for _ in range(S):
        increase()

    print(tube[X - 1][Y - 1])
