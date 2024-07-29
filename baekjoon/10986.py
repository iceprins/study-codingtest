import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    A = list(map(int, sys.stdin.readline().strip().split()))
    s = 0
    remainder = [0] * M

    for i in range(N):
        s += A[i]
        remainder[s % M] += 1

    result = remainder[0]

    for i in remainder:
        result += i * (i - 1) // 2

    print(result)
