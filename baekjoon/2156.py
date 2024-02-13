import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    pos = [0]
    dp = [0] * (n + 1)

    for _ in range(n):
        pos.append(int(sys.stdin.readline().strip()))

    for i in range(1, n + 1):
        if i == 1:
            dp[i] = pos[i]
        elif i == 2:
            dp[i] = dp[i - 1] + pos[i]
        elif i == 3:
            dp[i] = max(pos[1] + pos[2], pos[1] + pos[3], pos[2] + pos[3])
        else:
            dp[i] = max(dp[i - 3] + pos[i - 1] + pos[i], dp[i - 2] + pos[i], dp[i - 1])

    print(dp[n])
