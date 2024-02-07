import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        k = int(sys.stdin.readline().strip())
        n = int(sys.stdin.readline().strip())

        dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

        for i in range(1, n + 1):
            dp[0][i] = i

        for i in range(1, k + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        print(dp[k][n])
