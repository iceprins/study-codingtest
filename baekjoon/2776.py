# 단순 풀이
import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        saw = set(map(int, sys.stdin.readline().strip().split()))
        M = int(sys.stdin.readline().strip())
        checked = list(map(int, sys.stdin.readline().strip().split()))

        for num in checked:
            if num in saw:
                print(1)
            else:
                print(0)


# 이분 탐색 풀이
import sys


def binary_search(lo, hi, target):
    while lo <= hi:
        mid = (lo + hi) // 2

        if saw[mid] == target:
            return 1
        elif saw[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1

    return 0


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        saw = sorted(list(map(int, sys.stdin.readline().strip().split())))
        M = int(sys.stdin.readline().strip())
        checked = list(map(int, sys.stdin.readline().strip().split()))

        for elem in checked:
            print(binary_search(0, N - 1, elem))
