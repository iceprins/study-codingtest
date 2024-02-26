import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    weights = [int(sys.stdin.readline().strip()) for _ in range(N)]

    weights.sort()
    ans = 0

    for i in range(N):
        ans = max(ans, weights[i] * (N - i))

    print(ans)
