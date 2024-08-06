import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))
    dp = [1] * N

    for i in range(N):
        target = A[i]
        for j in range(i + 1, N):
            if A[j] > target:
                if dp[j] <= dp[i]:
                    dp[j] = dp[i] + 1
                else:
                    continue

    max_val = max(dp)
    max_idx = -1
    ans = []

    for i in range(len(dp) - 1, -1, -1):
        if dp[i] == max_val:
            max_idx = i
            ans.append(A[i])
            break

    next_val = max_val - 1

    for i in range(max_idx, -1, -1):
        if dp[i] == next_val:
            ans.append(A[i])
            next_val -= 1

    print(len(ans))
    print(*list(reversed(ans)))
