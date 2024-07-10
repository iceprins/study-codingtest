import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    size = sorted(list(map(int, sys.stdin.readline().strip().split())))
    res = 0

    for i in range(N - 1):
        start, end = i + 1, N - 1
        t = -1
        while start <= end:
            mid = (start + end) // 2
            if size[i] >= 0.9 * size[mid]:
                t = mid
                start = mid + 1
            else:
                end = mid - 1
        res += t - i if t > -1 else 0

    print(res)
