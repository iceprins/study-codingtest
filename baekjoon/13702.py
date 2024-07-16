import sys

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().strip().split())
    drinks = [int(sys.stdin.readline().strip()) for _ in range(N)]

    start, end = 1, max(drinks)
    vol = 0

    while start <= end:
        mid = (start + end) // 2

        cnt = 0

        for drink in drinks:
            cnt += (drink // mid)

        if cnt >= K:
            vol = mid
            start = mid + 1
        else:
            end = mid - 1

    print(vol)
