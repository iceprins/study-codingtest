import sys


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return right


if __name__ == '__main__':
    M, N, L = map(int, sys.stdin.readline().strip().split())
    lanes = sorted(list(map(int, sys.stdin.readline().strip().split())))
    cnt = 0

    for _ in range(N):
        x, y = map(int, sys.stdin.readline().strip().split())
        idx = binary_search(lanes, x)

        dist = abs(x - lanes[idx]) + y
        dist_right = abs(x - lanes[idx + 1]) + y if idx < M - 1 else float('inf')

        dist = min(dist, dist_right)

        if dist <= L:
            cnt += 1

    print(cnt)
