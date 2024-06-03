import sys
from collections import deque


def rotate():
    rotate_idx = []

    for i in range(4):
        rotate_idx.append([wheels[i][6], wheels[i][2]])

    target, direction = map(int, sys.stdin.readline().strip().split())
    target -= 1

    if target != 0:
        for i in range(target, 0, -1):
            if rotate_idx[i][0] != rotate_idx[i - 1][1]:
                if (target - (i - 1)) % 2 == 0:
                    wheels[i - 1].rotate(direction)
                else:
                    wheels[i - 1].rotate(-direction)
            else:
                break

    if target != 3:
        for i in range(target, 3):
            if rotate_idx[i][1] != rotate_idx[i + 1][0]:
                if (target - (i + 1) % 2) == 0:
                    wheels[i + 1].rotate(direction)
                else:
                    wheels[i + 1].rotate(-direction)
            else:
                break

    wheels[target].rotate(direction)


if __name__ == '__main__':
    wheels = [deque(list(map(int, sys.stdin.readline().strip()))) for _ in range(4)]

    K = int(sys.stdin.readline().strip())

    for _ in range(K):
        rotate()

    score = 0

    if wheels[0][0] == 1:
        score += 1
    if wheels[1][0] == 1:
        score += 2
    if wheels[2][0] == 1:
        score += 4
    if wheels[3][0] == 1:
        score += 8

    print(score)
