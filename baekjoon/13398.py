import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    seq = list(map(int, sys.stdin.readline().strip().split()))
    dp = [[i for i in seq] for _ in range(2)]

    for i in range(1, n):
        dp[0][i] = max(dp[0][i - 1] + seq[i], dp[0][i])
        dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + seq[i])

    print(max(max(dp[0]), max(dp[1])))
