import sys

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().strip().split())
    coins = [int(sys.stdin.readline().strip()) for _ in range(n)]
    ans = sys.maxsize

    dp = [10001] * (k + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[k] == 10001:
        print(-1)
    else:
        print(dp[k])
