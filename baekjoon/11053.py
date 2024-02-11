import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    sequence = list(map(int, sys.stdin.readline().strip().split()))
    dp = [1] * N

    for i in range(1, N):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))
