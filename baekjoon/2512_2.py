import sys


def calculate(n):
    result = 0
    for budget in budgets:
        if budget >= n:
            result += n
        else:
            result += budget

    return result


def search(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if calculate(mid) == target:
            return mid
        elif calculate(mid) > target:
            right = mid - 1
        else:
            left = mid + 1

    return right


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    budgets = sorted(list(map(int, sys.stdin.readline().strip().split())))
    total = int(sys.stdin.readline().strip())

    print(search(0, budgets[-1], total))
