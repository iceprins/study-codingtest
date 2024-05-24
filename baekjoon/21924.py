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
    global cnt
    ans = 0
    for connection in connections:
        cost, a, b = connection
        if find(a) != find(b):
            union(a, b)
            cnt += 1
            ans += cost

    return ans


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    parents = [i for i in range(N + 1)]
    connections = []

    origin, cnt = 0, 0

    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        origin += c
        connections.append((c, a, b))

    connections.sort()

    saved = kruskal()

    if cnt != N - 1:
        print(-1)
    else:
        print(origin - saved)


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
    graph = [[] for _ in range(N + 1)]

    origin = 0

    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        origin += c
        graph[a].append((c, b))
        graph[b].append((c, a))

    result = prim(1)

    if result == -1:
        print(result)
    else:
        print(origin - result)
