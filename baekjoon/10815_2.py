import sys


def binary_search(left, right, target):
    if left > right:
        return 0

    mid = (left + right) // 2

    if cards[mid] == target:
        return 1
    elif cards[mid] > target:
        right = mid - 1
    else:
        left = mid + 1

    return binary_search(left, right, target)


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    cards = list(map(int, sys.stdin.readline().strip().split()))
    M = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    result = list()

    cards.sort()

    for num in nums:
        result.append(binary_search(0, len(cards) - 1, num))

    print(*result)
