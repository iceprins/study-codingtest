import sys


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def kruskal():
    tot = 0
    for possible in possibles:
        dist, a, b = possible
        if find(a) != find(b):
            union(a, b)
            tot += dist
    return tot


def get_dist(idx1, idx2):
    return ((space_god[idx1][0] - space_god[idx2][0]) ** 2 + (space_god[idx1][1] - space_god[idx2][1]) ** 2) ** 0.5


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    space_god = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    parents = [i for i in range(N + 1)]

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())
        union(a, b)

    possibles = []

    for i in range(N):
        for j in range(i + 1, N):
            possibles.append((get_dist(i, j), i + 1, j + 1))

    possibles.sort()

    print("{:.2f}".format(kruskal()))
