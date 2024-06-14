import sys


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


if __name__ == '__main__':
    while True:
        m, n = map(int, sys.stdin.readline().strip().split())
        parents = [i for i in range(m)]
        connections = []

        if m == 0 and n == 0:
            break

        for _ in range(n):
            x, y, z = map(int, sys.stdin.readline().strip().split())
            connections.append((z, x, y))

        connections.sort()

        tot = 0

        for connection in connections:
            dist, x, y = connection
            if find(x) != find(y):
                union(x, y)
            else:
                tot += dist

        print(tot)
