import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        dp = [0] * (N + 1)

        for i in range(1, N + 1):
            if i == 1:
                dp[i] = 1
            elif i == 2:
                dp[i] = 1
            else:
                dp[i] = dp[i - 2] + dp[i - 3]

        print(dp[N])
