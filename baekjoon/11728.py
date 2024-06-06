import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    A = list(map(int, sys.stdin.readline().strip().split()))
    B = list(map(int, sys.stdin.readline().strip().split()))
    ans = []

    idx_A = 0
    idx_B = 0

    while idx_A < N and idx_B < M:
        if A[idx_A] <= B[idx_B]:
            ans.append(A[idx_A])
            idx_A += 1
        else:
            ans.append(B[idx_B])
            idx_B += 1

    if idx_A == N:
        ans += B[idx_B:]
    else:
        ans += A[idx_A:]

    print(*ans)
