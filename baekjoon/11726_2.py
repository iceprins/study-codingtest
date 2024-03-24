if __name__ == '__main__':
    n = int(input())
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        else:
            dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

    print(dp[n])