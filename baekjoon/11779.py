import sys
import heapq

INF = sys.maxsize


def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, [distance[start], start])

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for next_node, next_dist in graph[node]:
            tmp = dist + next_dist
            if tmp < distance[next_node]:
                distance[next_node] = tmp
                nearest[next_node] = node
                heapq.heappush(q, [tmp, next_node])


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        graph[a].append((b, c))

    departure, arrival = map(int, sys.stdin.readline().strip().split())

    distance = [INF] * (n + 1)
    nearest = [departure] * (n + 1)

    dijkstra(departure)

    ans = []
    tmp = arrival

    while tmp != departure:
        ans.append(tmp)
        tmp = nearest[tmp]

    ans.append(departure)
    ans.reverse()

    print(distance[arrival])
    print(len(ans))
    print(*ans)
