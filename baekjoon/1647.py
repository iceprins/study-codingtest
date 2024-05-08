import sys


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    parent = [i for i in range(N + 1)]
    edges = []

    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        edges.append((a, b, c))

    edges.sort(key=lambda x: x[2])

    ans = 0
    last_edge = 0

    for a, b, c in edges:
        if find(a) != find(b):
            union(a, b)
            ans += c
            last_edge = c

    print(ans - last_edge)
