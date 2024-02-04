import sys


def calculate(m, n, a, b):
    k = x
    while k <= m * n:
        if (k - a) % m == 0 and (k - b) % n == 0:
            return k
        k += m
    return -1


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        M, N, x, y = map(int, sys.stdin.readline().strip().split())

        print(calculate(M, N, x, y))
