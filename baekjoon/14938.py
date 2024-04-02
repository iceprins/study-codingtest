# 플로이드 워셜 풀이
import sys

INF = sys.maxsize

if __name__ == '__main__':
    n, m, r = map(int, sys.stdin.readline().strip().split())
    items = [0] + list(map(int, sys.stdin.readline().strip().split()))

    graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        graph[i][i] = 0
        graph[i][0] = 0
        graph[0][i] = 0

    for _ in range(r):
        a, b, l = map(int, sys.stdin.readline().strip().split())
        graph[a][b] = l
        graph[b][a] = l

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    ans = 0

    for i in range(1, n + 1):
        tmp = 0
        for j in range(1, n + 1):
            if graph[i][j] <= m:
                tmp += items[j]
        ans = max(ans, tmp)

    print(ans)


# 다익스트라 풀이
import sys
import heapq

INF = sys.maxsize


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


if __name__ == '__main__':
    n, m, r = map(int, sys.stdin.readline().strip().split())
    items = [0] + list(map(int, sys.stdin.readline().strip().split()))

    graph = [[] for _ in range(n + 1)]

    for _ in range(r):
        a, b, l = map(int, sys.stdin.readline().strip().split())
        graph[a].append([b, l])
        graph[b].append([a, l])

    ans = 0

    for i in range(1, n + 1):
        distance = [INF] * (n + 1)
        dijkstra(i)
        tmp = 0
        for j in range(1, n + 1):
            if distance[j] <= m:
                tmp += items[j]

        ans = max(ans, tmp)

    print(ans)
