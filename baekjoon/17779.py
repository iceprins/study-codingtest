import sys


def count(x, y, d1, d2):
    cnt = [0, 0, 0, 0, 0]
    fifth = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    for i in range(d1 + 1):
        fifth[x + i][y - i] = 1
        fifth[x + d2 + i][y + d2 - i] = 1
    for j in range(d2 + 1):
        fifth[x + j][y + j] = 1
        fifth[x + d1 + j][y - d1 + j] = 1
    for i in range(x + 1, x + d1 + d2):
        flag = False
        for j in range(N + 1):
            if fifth[i][j] == 1:
                if flag:
                    flag = False
                else:
                    flag = True
            else:
                if flag:
                    fifth[i][j] = 1

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i < x + d1 and j <= y and fifth[i][j] != 1:
                cnt[0] += population[i][j]
            elif i <= x + d2 and y < j and fifth[i][j] != 1:
                cnt[1] += population[i][j]
            elif x + d1 <= i and j < y - d1 + d2 and fifth[i][j] != 1:
                cnt[2] += population[i][j]
            elif x + d2 < i and y - d1 + d2 <= j and fifth[i][j] != 1:
                cnt[3] += population[i][j]
            elif fifth[i][j] == 1:
                cnt[4] += population[i][j]

    return max(cnt) - min(cnt)


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    population = [[]]

    for _ in range(N):
        population.append([0] + list(map(int, sys.stdin.readline().strip().split())))

    min_cnt = float('inf')
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            for d1 in range(1, N + 1):
                for d2 in range(1, N + 1):
                    if 1 <= x < x + d1 + d2 <= N and 1 <= y - d1 < y < y + d2 <= N:
                        min_cnt = min(min_cnt, count(x, y, d1, d2))

    print(min_cnt)
