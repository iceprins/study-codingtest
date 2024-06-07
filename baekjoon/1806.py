import sys

if __name__ == '__main__':
    N, S = map(int, sys.stdin.readline().strip().split())
    sequence = list(map(int, sys.stdin.readline().strip().split()))

    start, end = 0, 0
    tmp = 0
    ans = sys.maxsize

    while True:
        if tmp >= S:
            ans = min(ans, end - start)
            tmp -= sequence[start]
            start += 1
        elif end == N:
            break
        else:
            tmp += sequence[end]
            end += 1

    if ans == sys.maxsize:
        print(0)
    else:
        print(ans)
