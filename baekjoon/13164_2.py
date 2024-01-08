import sys

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().strip().split())
    heights = list(map(int, sys.stdin.readline().strip().split()))
    difference = list()

    if K == 1:
        print(heights[-1] - heights[0])
    else:
        ans = 0

        for i in range(1, len(heights)):
            difference.append(heights[i] - heights[i - 1])

        difference.sort(reverse=True)

        for i in range(K - 1):
            ans += difference[i]

        print(sum(difference) - ans)