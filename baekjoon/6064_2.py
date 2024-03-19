import sys


def calculate():
    k = x
    while k <= M * N:
        if (k - x) % M == 0 and (k - y) % N == 0:
            return k
        k += M
    return -1


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        M, N, x, y = map(int, sys.stdin.readline().strip().split())
        print(calculate())
