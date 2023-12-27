import sys

if __name__ == '__main__':
    children, group = map(int, sys.stdin.readline().strip().split())
    height = list(map(int, sys.stdin.readline().strip().split()))
    height_diff = list()

    for i in range(children - 1):
        height_diff.append(height[i+1] - height[i])

    height_diff.sort(reverse=True)

    cost = 0
    for i in range(group - 1):
        cost += height_diff[i]

    min_cost = height[children - 1] - height[0] - cost

    print(min_cost)