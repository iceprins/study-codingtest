import sys
from math import gcd
from math import sqrt

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    nums = sorted([int(sys.stdin.readline().strip()) for _ in range(N)])

    diff = []

    for i in range(1, N):
        diff.append(nums[i] - nums[i - 1])

    tmp = diff[0]

    for i in range(1, len(diff)):
        tmp = gcd(tmp, diff[i])

    ans = []

    for i in range(2, int(sqrt(tmp)) + 1):
        if tmp % i == 0:
            ans.append(i)
            ans.append(tmp // i)

    ans.append(tmp)
    ans = sorted(list(set(ans)))

    print(*ans)
