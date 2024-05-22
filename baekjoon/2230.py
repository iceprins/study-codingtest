import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    A = [int(sys.stdin.readline().strip()) for _ in range(N)]

    A.sort()

    start = 0
    end = 0
    ans = sys.maxsize

    while start <= N - 1 and end <= N - 1:
        diff = abs(A[start] - A[end])
        if diff < M:
            end += 1
        elif diff > M:
            ans = min(ans, diff)
            start += 1
        else:
            ans = diff
            break

    print(ans)
