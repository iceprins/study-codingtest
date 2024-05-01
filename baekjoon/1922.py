import sys


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())
    parent = [i for i in range(N + 1)]

    connects = []

    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        connects.append((c, a, b))

    connects.sort()
    ans = 0

    for connect in connects:
        cost, node1, node2 = connect

        if find(node1) != find(node2):
            union(node1, node2)
            ans += cost

    print(ans)
