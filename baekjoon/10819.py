import sys
from itertools import permutations


def calculate(nums):
    result = 0
    for i in range(len(nums) - 1):
        result += abs(nums[i + 1] - nums[i])
    return result


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    results = list()

    for i in permutations(arr, N):
        results.append(calculate(i))

    print(max(results))
