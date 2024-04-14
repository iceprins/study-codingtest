import sys

if __name__ == '__main__':
    lines = int(sys.stdin.readline().strip())
    pairs = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(lines)]

    pairs.sort(key=lambda x: x[0])

    dp = [1] * lines

    for i in range(lines - 1):
        for j in range(i + 1, lines):
            if pairs[i][1] < pairs[j][1]:
                dp[j] = max(dp[j], dp[i] + 1)

    print(lines - max(dp))
