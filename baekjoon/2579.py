import sys

if __name__ == '__main__':
    stairs = int(sys.stdin.readline().strip())
    scores = [0]

    for _ in range(stairs):
        scores.append(int(sys.stdin.readline().strip()))

    dp = [[0 for _ in range(2)] for _ in range(stairs + 1)]

    for i in range(1, stairs + 1):
        if i == 1:
            dp[i][0] = scores[i]
            dp[i][1] = scores[i]
        elif i == 2:
            dp[i][0] = scores[i]
            dp[i][1] = scores[i] + scores[i - 1]
        else:
            dp[i][0] = max(dp[i - 2][0], dp[i - 2][1]) + scores[i]
            dp[i][1] = dp[i - 1][0] + scores[i]

    print(max(dp[stairs]))
