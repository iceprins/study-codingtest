import sys
import heapq


def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, [distance[start], start])

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for next_node, next_dist in route_map[node]:
            tmp = dist + next_dist
            if tmp < distance[next_node]:
                distance[next_node] = tmp
                heapq.heappush(q, (tmp, next_node))

    return distance


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())

    route_map = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    distance = [sys.maxsize] * (N + 1)

    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        route_map[a].append((b, c))

    depart, dest = map(int, sys.stdin.readline().strip().split())

    dijkstra(depart)

    print(distance[dest])
