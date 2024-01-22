import sys


def convert(condition, cnt):
    for i in range(1, N - 1):
        if condition[i - 1] != after[i - 1]:
            cnt += 1
            for j in range(i - 1, i + 2):
                condition[j] = 1 - condition[j]

    if condition[N - 1] != after[N - 1]:
        cnt += 1
        condition[N - 2] = 1 - condition[N - 2]
        condition[N - 1] = 1 - condition[N - 1]

    if condition == after:
        return cnt
    return -1


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    before_1 = list(map(int, sys.stdin.readline().strip()))
    after = list(map(int, sys.stdin.readline().strip()))

    before_2 = before_1.copy()
    before_2[0] = 1 - before_2[0]
    before_2[1] = 1 - before_2[1]

    if after == before_1:
        print(0)
    else:
        result = convert(before_1, 0)
        if result != -1:
            print(result)
        else:
            result = convert(before_2, 1)
            print(result)
