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
    ans, cnt = 0, 0

    for connection in connections:
        cost, a, b = connection
        if find(a) != find(b):
            union(a, b)
            ans += cost
            cnt += 1

    if cnt == N - 1:
        return ans

    return -1


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    info = list(sys.stdin.readline().strip().split())
    parents = [i for i in range(N + 1)]
    connections = []

    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        if info[a - 1] != info[b - 1]:
            connections.append((c, a, b))

    connections.sort()

    print(kruskal())


# Prim 풀이
import sys
import heapq


def prim(start):
    q = []
    selected = [False] * (N + 1)

    heapq.heappush(q, (0, start))

    ans, cnt = 0, 0

    while q:
        if cnt == N:
            return ans
        cost, vertex = heapq.heappop(q)
        if not selected[vertex]:
            selected[vertex] = True
            ans += cost
            cnt += 1
            for i in graph[vertex]:
                heapq.heappush(q, i)

    return -1


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    info = list(sys.stdin.readline().strip().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        if info[a - 1] != info[b - 1]:
            graph[a].append((c, b))
            graph[b].append((c, a))

    print(prim(1))
