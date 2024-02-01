import sys


def dfs(depth, arr, value):
    global max_val, min_val
    if depth == N:
        max_val = max(max_val, value)
        min_val = min(min_val, value)
        return

    if arr[0] > 0:
        arr[0] -= 1
        dfs(depth + 1, arr, value + nums[depth])
        arr[0] += 1
    if arr[1] > 0:
        arr[1] -= 1
        dfs(depth + 1, arr, value - nums[depth])
        arr[1] += 1
    if arr[2] > 0:
        arr[2] -= 1
        dfs(depth + 1, arr, value * nums[depth])
        arr[2] += 1
    if arr[3] > 0:
        arr[3] -= 1
        dfs(depth + 1, arr, int(value / nums[depth]))
        arr[3] += 1


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    op = list(map(int, sys.stdin.readline().strip().split()))

    max_val = -sys.maxsize
    min_val = sys.maxsize

    dfs(1, op, nums[0])

    print(max_val)
    print(min_val)
