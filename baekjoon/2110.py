import sys

if __name__ == '__main__':
    N, C = map(int, sys.stdin.readline().strip().split())
    houses = [int(sys.stdin.readline().strip()) for _ in range(N)]

    houses.sort()

    start = 1
    end = houses[-1] - houses[0]
    result = 0

    while start <= end:
        mid = (start + end) // 2
        current = houses[0]
        cnt = 1

        for i in range(1, N):
            if houses[i] >= current + mid:
                cnt += 1
                current = houses[i]

        if cnt >= C:
            start = mid + 1
            result = mid
        else:
            end = mid - 1

    print(result)
