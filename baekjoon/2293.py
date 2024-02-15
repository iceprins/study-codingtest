import sys

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().strip().split())
    value = list(int(sys.stdin.readline().strip()) for _ in range(n))

    value.sort()

    dp = [0] * (k + 1)
    dp[0] = 1

    for v in value:
        for i in range(v, k + 1):
            dp[i] += dp[i - v]

    print(dp[k])
