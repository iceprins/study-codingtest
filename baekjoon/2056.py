import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        work_time, precedence, *works = map(int, sys.stdin.readline().strip().split())
        dp[i] = work_time
        for j in works:
            dp[i] = max(dp[i], dp[j] + work_time)

    print(max(dp))
