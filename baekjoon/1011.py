import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        x, y = map(int, sys.stdin.readline().strip().split())
        dist = y - x
        tmp = 0
        cnt = 0
        loop = 0

        while tmp < dist:
            cnt += 1
            if cnt % 2 != 0:
                loop += 1
            tmp += loop

        print(cnt)
