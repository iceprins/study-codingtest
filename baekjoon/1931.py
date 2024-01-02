import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    schedules = list()

    for _ in range(N):
        pair = tuple(map(int, sys.stdin.readline().strip().split()))
        schedules.append(pair)

    schedules.sort(key=lambda x:x[0])
    schedules.sort(key=lambda x:x[1])

    right_boundary = 0
    cnt = 0

    for i in range(N):
        if schedules[i][0] >= right_boundary:
            right_boundary = schedules[i][1]
            cnt += 1

    print(cnt)