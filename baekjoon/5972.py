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
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))

    return distance[-1]


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    print(dijkstra(1))
