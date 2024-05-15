import sys
import heapq


def dijkstra(start):
    dist = [sys.maxsize] * (N + 1)
    dist[start] = 0
    q = []
    heapq.heappush(q, [dist[start], start])

    while q:
        now_dist, now_node = heapq.heappop(q)

        if dist[now_node] < now_dist:
            continue

        for next_node, next_dist in graph[now_node]:
            tmp = now_dist + next_dist
            if tmp < dist[next_node]:
                dist[next_node] = tmp
                heapq.heappush(q, (tmp, next_node))

    return dist


if __name__ == '__main__':
    N, E = map(int, sys.stdin.readline().strip().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(E):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    v1, v2 = map(int, sys.stdin.readline().strip().split())

    from_1 = dijkstra(1)
    from_v1 = dijkstra(v1)
    from_v2 = dijkstra(v2)

    opt_1 = from_1[v1] + from_v1[v2] + from_v2[N]
    opt_2 = from_1[v2] + from_v2[v1] + from_v1[N]

    ans = min(opt_1, opt_2)

    print(ans if ans < sys.maxsize else -1)
