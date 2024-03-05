import sys

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().strip().split())
    heights = sorted(list(map(int, sys.stdin.readline().strip().split())))
    gap = list()

    for i in range(N - 1):
        gap.append(heights[i + 1] - heights[i])

    gap.sort(reverse=True)

    print(sum(gap[K - 1:]))
