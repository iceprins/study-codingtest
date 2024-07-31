import sys
from collections import deque

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def spring():
    for i in range(N):
        for j in range(N):
            for k in range(len(age[i][j])):
                if nutrient[i][j] < age[i][j][k]:
                    for _ in range(k, len(age[i][j])):
                        dead[i][j].append(age[i][j].pop())
                    break
                else:
                    nutrient[i][j] -= age[i][j][k]
                    age[i][j][k] += 1


def summer():
    for i in range(N):
        for j in range(N):
            dead_trees = dead[i][j]
            while dead_trees:
                nutrient[i][j] += dead_trees.pop() // 2


def fall():
    for i in range(N):
        for j in range(N):
            for k in range(len(age[i][j])):
                if age[i][j][k] % 5 == 0:
                    for k in range(8):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                            continue
                        age[nx][ny].appendleft(1)


def winter():
    for i in range(N):
        for j in range(N):
            nutrient[i][j] += A[i][j]


if __name__ == '__main__':
    N, M, K = map(int, sys.stdin.readline().strip().split())
    A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    age = [[deque() for _ in range(N)] for _ in range(N)]
    nutrient = [[5] * N for _ in range(N)]
    dead = [[[] for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        x, y, z = map(int, sys.stdin.readline().strip().split())
        age[x - 1][y - 1].append(z)

    for i in range(K):
        spring()
        summer()
        fall()
        winter()

    ans = 0

    for i in range(N):
        for j in range(N):
            ans += len(age[i][j])

    print(ans)
