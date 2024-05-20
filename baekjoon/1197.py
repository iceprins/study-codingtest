# Prim 풀이
import sys
import heapq


def prim(start):
    q = []
    selected = [False] * (V + 1)

    heapq.heappush(q, (0, start))

    ans = 0
    cnt = 0

    while q:
        if cnt == V:
            break
        cost, vertex = heapq.heappop(q)
        if not selected[vertex]:
            selected[vertex] = True
            ans += cost
            cnt += 1
            for i in G[vertex]:
                heapq.heappush(q, i)

    return ans


if __name__ == '__main__':
    V, E = map(int, sys.stdin.readline().strip().split())
    G = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        G[a].append((c, b))
        G[b].append((c, a))

    print(prim(1))


# Kruskal 풀이
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


def kruskal():
    ans = 0

    for connect in connects:
        cost, a, b = connect
        if find(a) != find(b):
            union(a, b)
            ans += cost

    return ans


if __name__ == '__main__':
    V, E = map(int, sys.stdin.readline().strip().split())
    connects = []
    parents = [i for i in range(V + 1)]

    for _ in range(E):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        connects.append((c, a, b))

    connects.sort()

    print(kruskal())
