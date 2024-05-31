import sys
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [sys.maxsize] * (N + 1)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            if dist + 1 < distance[i]:
                distance[i] = dist + 1
                heapq.heappush(q, (dist + 1, i))

    return distance


if __name__ == '__main__':
    N, M, K, X = map(int, sys.stdin.readline().strip().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a].append(b)

    result = dijkstra(X)
    ans = []

    for i in range(N + 1):
        if result[i] == K:
            ans.append(i)

    if len(ans) == 0:
        print(-1)
    else:
        for elem in ans:
            print(elem)
