import sys

dx = [0, 1, 1]
dy = [1, 0, 1]


def dfs(x, y, condition):
    if x == N - 1 and y == N - 1:
        result.append(1)
        return

    if condition == 0 or condition == 2:
        if y + 1 < N and house[x][y + 1] == 0:
            dfs(x, y + 1, 0)

    if condition == 1 or condition == 2:
        if x + 1 < N and house[x + 1][y] == 0:
            dfs(x + 1, y, 1)

    if condition == 0 or condition == 1 or condition == 2:
        if x + 1 < N and y + 1 < N and house[x + 1][y] == 0 and house[x][y + 1] == 0 and house[x + 1][y + 1] == 0:
            dfs(x + 1, y + 1, 2)


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    house = list()
    result = list()

    for _ in range(N):
        house.append(list(map(int, sys.stdin.readline().strip().split())))

    dfs(0, 1, 0)

    print(len(result))
