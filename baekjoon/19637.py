import sys
from bisect import bisect_left

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    title = []
    power = []

    for _ in range(N):
        a, b = sys.stdin.readline().strip().split()
        title.append(a)
        power.append(int(b))

    for _ in range(M):
        print(title[bisect_left(power, int(sys.stdin.readline().strip()))])
