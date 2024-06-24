import sys


def find(x):
    global ans
    cnt = 1
    now_min = 10000
    now_max = 0
    for i in range(N):
        now_min = min(now_min, arr[i])
        now_max = max(now_max, arr[i])

        if now_max - now_min > x:
            cnt += 1
            now_min = now_max = arr[i]

    return cnt


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    ans = sys.maxsize
    left, right = 0, max(arr)

    while left <= right:
        mid = (left + right) // 2

        if find(mid) <= M:
            right = mid - 1
            ans = min(mid, ans)
        else:
            left = mid + 1

    print(ans)
