import sys


def search(left, right, target):
    while left <= right:
        mid = (left + right) // 2

        if A[mid] == target:
            return 1
        elif A[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return 0


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))
    M = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split()))

    A.sort()

    for num in nums:
        print(search(0, N - 1, num))
