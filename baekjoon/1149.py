import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    cost = list()
    dp = [0] * 3

    for _ in range(N):
        cost.append(list(map(int, sys.stdin.readline().strip().split())))

    dp[0] = cost[1][0] + min(cost[0][1], cost[0][2])
    dp[1] = cost[1][1] + min(cost[0][0], cost[0][2])
    dp[2] = cost[1][2] + min(cost[0][0], cost[0][1])

    for i in range(2, N):
        a = min(dp[1] + cost[i][0], dp[2] + cost[i][0])
        b = min(dp[0] + cost[i][1], dp[2] + cost[i][1])
        c = min(dp[0] + cost[i][2], dp[1] + cost[i][2])
        dp[0], dp[1], dp[2] = a, b, c

    print(min(dp))
