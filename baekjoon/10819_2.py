import sys
from itertools import permutations


def calculate(numbers):
    result = 0

    for i in range(len(numbers) - 1):
        result += abs(numbers[i] - numbers[i + 1])

    return result


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))
    cand = list(permutations(A, N))
    ans = 0

    for elem in cand:
        ans = max(ans, calculate(elem))

    print(ans)
