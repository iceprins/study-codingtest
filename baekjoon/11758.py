import sys


def ccw(p1, p2, p3):
    return p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - (p2[0] * p1[1] + p3[0] * p2[1] + p1[0] * p3[1])


if __name__ == '__main__':
    P = []

    for _ in range(3):
        P.append(tuple(map(int, sys.stdin.readline().strip().split())))

    ans = ccw(P[0], P[1], P[2])

    if ans > 0:
        print(1)
    elif ans == 0:
        print(0)
    else:
        print(-1)
