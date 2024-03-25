import sys

if __name__ == '__main__':
    stairs = int(sys.stdin.readline().strip())
    scores = [0]

    for _ in range(stairs):
        scores.append(int(sys.stdin.readline().strip()))

    dp = [0] * (stairs + 1)

    for i in range(1, stairs + 1):
        if i == 1:
            dp[i] = scores[1]
        elif i == 2:
            dp[i] = scores[1] + scores[2]
        else:
            dp[i] = max(dp[i - 3] + scores[i - 1] + scores[i], dp[i - 2] + scores[i])

    print(dp[stairs])
