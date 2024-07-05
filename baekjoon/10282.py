import sys
import heapq


def dijkstra(start):
    heapq.heappush(heap, [0, start])
    dist[start] = 0
    while heap:
        c_cost, c_vertex = heapq.heappop(heap)
        for n_vertex, n_cost in graph[c_vertex]:
            tmp = c_cost + n_cost
            if tmp < dist[n_vertex]:
                dist[n_vertex] = tmp
                heapq.heappush(heap, [tmp, n_vertex])


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        n, d, c = map(int, sys.stdin.readline().strip().split())
        graph = [[] for _ in range(n + 1)]
        dist = [sys.maxsize] * (n + 1)
        heap = []

        for _ in range(d):
            a, b, s = map(int, sys.stdin.readline().strip().split())
            graph[b].append([a, s])

        dijkstra(c)

        cnt = 0
        ans = 0

        for i in dist:
            if i != sys.maxsize:
                cnt += 1
                ans = max(ans, i)

        print(cnt, ans)
