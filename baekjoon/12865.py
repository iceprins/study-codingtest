import sys

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().strip().split())
    items = list(list(map(int, sys.stdin.readline().strip().split())) for _ in range(N))
    dp = [0 for _ in range(K + 1)]

    for item in items:
        w, v = item
        for i in range(K, w - 1, -1):
            dp[i] = max(dp[i], dp[i - w] + v)

    print(dp[-1])
