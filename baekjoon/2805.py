import sys


def calculate(n):
    result = 0
    for height in heights:
        if height > n:
            result += (height - n)
    return result


def search(left, right, target):
    while left <= right:
        mid = (left + right) // 2

        if calculate(mid) == target:
            return mid
        elif calculate(mid) > target:
            left = mid + 1
        else:
            right = mid - 1

    return left - 1


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    heights = list(map(int, sys.stdin.readline().strip().split()))

    heights.sort()

    print(search(0, heights[-1], M))
