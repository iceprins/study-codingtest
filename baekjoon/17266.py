import sys


def check(height):
    load = []

    for x in pos:
        tmp1 = x - height
        tmp2 = x + height
        if len(load) == 0:
            load.append([tmp1, tmp2])
        else:
            a, b = load.pop()
            if tmp1 <= b:
                load.append([a, tmp2])
            else:
                load.append([a, b])
                load.append([tmp1, tmp2])

    if len(load) > 1:
        return False
    elif load[0][0] > 0 or load[0][1] < N:
        return False
    else:
        return True


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())
    pos = list(map(int, sys.stdin.readline().strip().split()))

    start, end = 1, N
    ans = sys.maxsize

    while start <= end:
        mid = (start + end) // 2

        if check(mid):
            ans = min(ans, mid)
            end = mid - 1
        else:
            start = mid + 1

    print(ans)
