import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    schedule = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

    dp = [0] * (N + 1)

    for i in range(N):
        for j in range(i + schedule[i][0], N + 1):
            if dp[j] < dp[i] + schedule[i][1]:
                dp[j] = dp[i] + schedule[i][1]

    print(dp[-1])
