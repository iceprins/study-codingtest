# binary_search 구현
import sys


def binary_search(target, opt):
    start, end = 0, N - 1

    while start <= end:
        mid = (start + end) // 2

        if spot[mid] == target:
            return mid
        elif spot[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    if opt == 0:
        return start
    else:
        return end


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    spot = sorted(list(map(int, sys.stdin.readline().strip().split())))

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())
        print(binary_search(b, 1) - binary_search(a, 0) + 1)


# bisect 이용
import sys
from bisect import bisect_left, bisect_right

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    spot = sorted(list(map(int, sys.stdin.readline().strip().split())))

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())
        print(bisect_right(spot, b) - bisect_left(spot, a))
