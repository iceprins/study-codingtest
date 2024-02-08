import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        dp = [[0 for _ in range(2)] for _ in range(N + 1)]

        for i in range(N + 1):
            if i == 0:
                dp[i][0] = 1
                dp[i][1] = 0
            elif i == 1:
                dp[i][0] = 0
                dp[i][1] = 1
            else:
                dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
                dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

        print(*dp[N])
