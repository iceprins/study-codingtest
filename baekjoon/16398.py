# Kruskal 풀이 (O(Elog_2E))
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
    for connection in connections:
        cost, a, b = connection
        if find(a) != find(b):
            union(a, b)
            ans += cost

    return ans


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    connections = []
    parents = [i for i in range(N + 1)]

    for i in range(N):
        C = list(map(int, sys.stdin.readline().strip().split()))
        for j in range(i + 1, N):
            connections.append((C[j], i + 1, j + 1))

    connections.sort()

    print(kruskal())


# Prim 풀이 (O(N^2))
import sys
import heapq


def prim(start):
    q = []
    selected = [False] * (N + 1)

    heapq.heappush(q, (0, start))

    ans = 0

    while q:
        cost, vertex = heapq.heappop(q)
        if not selected[vertex]:
            selected[vertex] = True
            ans += cost
            for i in graph[vertex]:
                heapq.heappush(q, i)

    return ans


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    graph = [[] for _ in range(N + 1)]

    for i in range(N):
        C = list(map(int, sys.stdin.readline().strip().split()))
        for j in range(N):
            if C[j] != 0:
                graph[i + 1].append((C[j], j + 1))

    print(prim(1))
