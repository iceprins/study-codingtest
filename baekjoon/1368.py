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
    cnt = 0
    tot = 0
    for connection in connections:
        cost, a, b = connection
        if find(a) != find(b):
            union(a, b)
            tot += cost
            cnt += 1
            if cnt >= N:
                break

    return tot


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    parents = [i for i in range(N + 1)]
    connections = []

    for i in range(1, N + 1):
        W = int(sys.stdin.readline().strip())
        connections.append((W, 0, i))

    for i in range(1, N + 1):
        P = list(map(int, sys.stdin.readline().strip().split()))
        for j in range(i + 1, N + 1):
            connections.append((P[j - 1], i, j))

    connections.sort()

    print(kruskal())
