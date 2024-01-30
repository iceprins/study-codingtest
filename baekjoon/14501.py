import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    plan = list()

    for _ in range(N):
        plan.append(tuple(map(int, sys.stdin.readline().strip().split())))

    dp = [0] * (N + 1)

    for i in range(N):
        for j in range(i + plan[i][0], N + 1):
            if dp[j] < dp[i] + plan[i][1]:
                dp[j] = dp[i] + plan[i][1]

    print(dp[-1])
