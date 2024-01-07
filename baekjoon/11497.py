import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        logs = list(map(int, sys.stdin.readline().strip().split()))

        logs.sort()

        ans = 0
        for i in range(N - 2):
            print(ans)
            ans = max(ans, logs[i + 2] - logs[i])

        ans = max(ans, logs[1] - logs[0])
        ans = max(ans, logs[-1] - logs[-2])

        print(ans)