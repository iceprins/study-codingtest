import sys

regions = int(sys.stdin.readline().strip())
budget = list(map(int, sys.stdin.readline().strip().split()))
max_budget = int(sys.stdin.readline().strip())


def calculate(arg):
    result = 0
    for elem in budget:
        if elem <= arg:
            result += elem
        else:
            result += arg
    return result


def search(start, end):
    while start <= end:
        mid = (start + end) // 2
        if calculate(mid) > max_budget:
            end = mid - 1
        else:
            start = mid + 1
    return end


if __name__ == '__main__':
    budget.sort()
    print(search(0, budget[-1]))