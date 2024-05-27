import sys

sys.setrecursionlimit(10 ** 6)


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
    n, m = map(int, sys.stdin.readline().strip().split())
    parents = [i for i in range(n + 1)]

    for _ in range(m):
        op, a, b = map(int, sys.stdin.readline().strip().split())

        if op == 0:
            union(a, b)
        else:
            if find(a) == find(b):
                print("YES")
            else:
                print("NO")
