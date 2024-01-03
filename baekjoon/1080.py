import sys

def trans_mat(mat, row, col):
    for i in range(3):
        for j in range(3):
            mat[row + i][col + j] = (mat[row + i][col + j] + 1) % 2
    return mat

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())

    before = list()
    after = list()
    cnt = 0

    for _ in range(N):
        before.append(list(map(int, sys.stdin.readline().strip())))
    for _ in range(N):
        after.append(list(map(int, sys.stdin.readline().strip())))

    if N < 3 or M < 3:
        if before == after:
            print(0)
        else:
            print(-1)
    else:
        for i in range(N - 2):
            for j in range(M - 2):
                if before[i][j] != after[i][j]:
                    trans_mat(before, i, j)
                    cnt += 1

        if before == after:
            print(cnt)
        else:
            print(-1)