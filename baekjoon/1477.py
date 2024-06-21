import sys

if __name__ == '__main__':
    N, M, L = map(int, sys.stdin.readline().strip().split())
    rest = [0, L]

    if N != 0:
        rest = [0] + sorted(list(map(int, sys.stdin.readline().strip().split()))) + [L]

    start, end = 1, L - 1
    result = 0

    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for i in range(1, len(rest)):
            if rest[i] - rest[i - 1] > mid:
                cnt += (rest[i] - rest[i - 1] - 1) // mid
        if cnt > M:
            start = mid + 1
        else:
            end = mid - 1
            result = mid

    print(result)
