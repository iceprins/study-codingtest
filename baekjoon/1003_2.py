import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        zero_dp = [0] * 41
        one_dp = [0] * 41

        zero_dp[0] = 1
        one_dp[1] = 1

        for i in range(2, N + 1):
            zero_dp[i] = zero_dp[i - 1] + zero_dp[i - 2]
            one_dp[i] = one_dp[i - 1] + one_dp[i - 2]

        print(zero_dp[N], one_dp[N])
