import sys
import heapq


def dijkstra(start):
    queue = list()
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


if __name__ == '__main__':
    V, E = map(int, sys.stdin.readline().strip().split())
    K = int(sys.stdin.readline().strip())
    graph = [[] for _ in range(V + 1)]
    distance = [sys.maxsize] * (V + 1)

    for _ in range(E):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        graph[a].append([b, c])

    dijkstra(K)

    for i in range(1, V + 1):
        if distance[i] == sys.maxsize:
            print("INF")
        else:
            print(distance[i])
