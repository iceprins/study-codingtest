import sys
import copy
from itertools import permutations


def rotate(r, c, s):
    ltx, lty = r - s - 1, c - s - 1
    rbx, rby = r + s - 1, c + s - 1

    graph = copy.deepcopy(tmp)

    for _ in range(s):
        # 상
        for i in range(lty, rby):
            tmp[ltx][i + 1] = graph[ltx][i]
        # 하
        for i in range(rby, lty, -1):
            tmp[rbx][i - 1] = graph[rbx][i]
        # 좌
        for i in range(rbx, ltx, -1):
            tmp[i - 1][lty] = graph[i][lty]
        # 우
        for i in range(ltx, rbx):
            tmp[i + 1][rby] = graph[i][rby]

        ltx += 1
        lty += 1
        rbx -= 1
        rby -= 1


if __name__ == '__main__':
    N, M, K = map(int, sys.stdin.readline().strip().split())
    A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    ops = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(K)]

    ans = sys.maxsize

    for case in permutations(ops):
        tmp = copy.deepcopy(A)

        for a, b, c in case:
            rotate(a, b, c)

        for arr in tmp:
            ans = min(ans, sum(arr))

    print(ans)
