import sys

if __name__ == '__main__':
    N, L = map(int, sys.stdin.readline().strip().split())
    holes = sorted(list(map(int, sys.stdin.readline().strip().split())))

    cnt = 1
    start = holes[0] + L - 1

    for hole in holes:
        if hole <= start:
            continue
        start = hole + L - 1
        cnt += 1

    print(cnt)
