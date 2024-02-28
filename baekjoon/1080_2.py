import sys


def transform(row, column):
    for i in range(3):
        for j in range(3):
            A[row + i][column + j] = (A[row + i][column + j] + 1) % 2


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    A = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
    B = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

    cnt = 0

    for i in range(N - 2):
        for j in range(M - 2):
            if A[i][j] != B[i][j]:
                transform(i, j)
                cnt += 1

    if A == B:
        print(cnt)
    else:
        print(-1)
