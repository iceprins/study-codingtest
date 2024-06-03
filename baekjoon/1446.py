import sys
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distances[now] < dist:
            continue

        for i in roads[now]:
            if dist + i[1] < distances[i[0]]:
                distances[i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))


if __name__ == '__main__':
    N, D = map(int, sys.stdin.readline().strip().split())
    roads = [[] for _ in range(D + 1)]
    distances = [sys.maxsize] * (D + 1)

    for i in range(D):
        roads[i].append((i + 1, 1))

    for _ in range(N):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        if b > D:
            continue
        roads[a].append((b, c))

    dijkstra(0)

    print(distances[D])
