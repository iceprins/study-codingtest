import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        heights = list(map(int, sys.stdin.readline().strip().split()))

        heights.sort()

        ans = 0

        for i in range(N - 2):
            ans = max(ans, heights[i + 2] - heights[i])

        ans = max(ans, heights[1] - heights[0])
        ans = max(ans, heights[-1] - heights[-2])

        print(ans)
