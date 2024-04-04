if __name__ == '__main__':
    N = int(input())
    dp = [0] * (N + 1)

    if N % 2 == 1:
        print(0)
    else:
        for i in range(2, N + 1, 2):
            if i == 2:
                dp[i] = 3
            else:
                dp[i] = dp[i - 2] * 3 + sum(dp[:i - 2]) * 2 + 2
        print(dp[N])
