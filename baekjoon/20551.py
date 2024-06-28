import sys


def binary_search(lo, hi, target):
    ans = sys.maxsize
    while lo <= hi:
        mid = (lo + hi) // 2
        if A[mid] == target:
            ans = min(ans, mid)
            hi = mid - 1
        elif A[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1

    if ans == sys.maxsize:
        return -1
    else:
        return ans


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    A = sorted([int(sys.stdin.readline().strip()) for _ in range(N)])

    for _ in range(M):
        D = int(sys.stdin.readline().strip())
        result = binary_search(0, N - 1, D)
        print(result)
