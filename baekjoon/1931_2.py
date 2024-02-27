import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    plans = sorted(list(tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)))

    plans.sort(key=lambda x: x[1])

    end = 0
    cnt = 0

    for plan in plans:
        if plan[0] >= end:
            end = plan[1]
            cnt += 1

    print(cnt)
