import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    heights = list(map(int, sys.stdin.readline().strip().split()))

    stack = []
    ans = [0] * N

    for i in range(N):
        while stack:
            if stack[-1][1] > heights[i]:
                ans[i] = stack[-1][0] + 1
                break
            else:
                stack.pop()
        stack.append((i, heights[i]))

    print(*ans)
