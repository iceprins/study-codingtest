import sys

if __name__ == '__main__':
    K, N = map(int, sys.stdin.readline().strip().split())
    lines = sorted([int(sys.stdin.readline().strip()) for _ in range(K)])

    start, end = 1, lines[-1]

    while start <= end:
        mid = (start + end) // 2
        n = 0

        for line in lines:
            n += line // mid

        if n >= N:
            start = mid + 1
        else:
            end = mid - 1

    print(end)
