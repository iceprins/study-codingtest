import sys
from collections import defaultdict


def R_fun():
    max_len = -1
    for i in range(len(A)):
        cnt_info = defaultdict(int)
        tmp = []
        for j in range(len(A[i])):
            cnt_info[A[i][j]] += 1

        for key in cnt_info:
            if key == 0:
                continue
            tmp.append([key, cnt_info[key]])

        tmp.sort(key=lambda x: (x[1], x[0]))

        arr = []

        for x in tmp:
            arr.extend(x)

        A[i] = arr

    for arr in A:
        max_len = max(max_len, len(arr))

    for arr in A:
        tmp = max_len - len(arr)
        if tmp == 0:
            continue
        for _ in range(tmp):
            arr.append(0)


def C_fun():
    global A
    A = list(map(list, zip(*A)))
    R_fun()
    A = list(map(list, zip(*A)))


if __name__ == '__main__':
    r, c, k = map(int, sys.stdin.readline().strip().split())
    A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(3)]
    cnt = 0

    while cnt <= 100:
        if 1 <= r <= len(A) and 1 <= c <= len(A[0]) and A[r - 1][c - 1] == k:
            break

        if len(A) >= len(A[0]):
            R_fun()
        else:
            C_fun()

        cnt += 1

    print(cnt if cnt <= 100 else -1)
