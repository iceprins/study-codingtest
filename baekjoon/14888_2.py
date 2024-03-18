import sys


def solve(idx, n):
    global max_result, min_result
    if idx == N:
        max_result = max(max_result, n)
        min_result = min(min_result, n)
        return
    if op[0] > 0:
        op[0] -= 1
        solve(idx + 1, n + A[idx])
        op[0] += 1
    if op[1] > 0:
        op[1] -= 1
        solve(idx + 1, n - A[idx])
        op[1] += 1
    if op[2] > 0:
        op[2] -= 1
        solve(idx + 1, n * A[idx])
        op[2] += 1
    if op[3] > 0:
        op[3] -= 1
        solve(idx + 1, int(n / A[idx]))
        op[3] += 1


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))
    op = list(map(int, sys.stdin.readline().strip().split()))

    max_result = -sys.maxsize
    min_result = sys.maxsize

    solve(1, A[0])

    print(max_result)
    print(min_result)
