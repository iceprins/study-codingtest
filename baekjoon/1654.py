import sys


def calculate(n):
    result = 0
    for line in lines:
        if line >= n:
            result += line // n

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

    return right


if __name__ == '__main__':
    K, N = map(int, sys.stdin.readline().strip().split())
    lines = list()

    for _ in range(K):
        lines.append(int(sys.stdin.readline().strip()))

    lines.sort()

    print(search(0, lines[-1], N))
