import sys
from collections import deque

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().strip().split())
    A = deque(list(map(int, sys.stdin.readline().strip().split())))
    belt = deque([False] * N)

    cnt = 0

    while True:
        cnt += 1

        A.rotate(1)
        belt.rotate(1)

        belt[N - 1] = False

        for i in range(N - 2, -1, -1):
            if belt[i] and not belt[i + 1] and A[i + 1] >= 1:
                belt[i], belt[i + 1] = False, True
                A[i + 1] -= 1

        belt[N - 1] = False

        if A[0] > 0:
            belt[0] = True
            A[0] -= 1

        if A.count(0) >= K:
            break

    print(cnt)
