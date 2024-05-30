# Dijkstra 풀이
# import sys
# import heapq
#
#
# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance = [sys.maxsize] * (n + 1)
#     distance[start] = 0
#     path[start] = [start]
#
#     while q:
#         dist, now = heapq.heappop(q)
#
#         if distance[now] < dist:
#             continue
#
#         for i in graph[now]:
#             if dist + i[1] < distance[i[0]]:
#                 distance[i[0]] = dist + i[1]
#                 heapq.heappush(q, (dist + i[1], i[0]))
#                 path[i[0]] = path[now] + [i[0]]
#
#     ans = []
#
#     for i in range(1, n + 1):
#         if i == start:
#             ans.append('-')
#         else:
#             ans.append(path[i][1])
#
#     return ans
#
#
# if __name__ == '__main__':
#     n, m = map(int, sys.stdin.readline().strip().split())
#     graph = [[] for _ in range(n + 1)]
#     path = [['-' for _ in range(n + 1)] for _ in range(n + 1)]
#
#     for _ in range(m):
#         a, b, c = map(int, sys.stdin.readline().strip().split())
#         graph[a].append((b, c))
#         graph[b].append((a, c))
#
#     for i in range(1, n + 1):
#         print(*dijkstra(i))


# Floyd_Warshall 풀이
import sys


def floyd_warshall():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    ans[i][j] = ans[i][k]


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().strip().split())
    graph = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]
    ans = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        graph[a][b] = graph[b][a] = c
        ans[a][b] = b
        ans[b][a] = a

    floyd_warshall()

    for i in range(1, n + 1):
        ans[i][i] = '-'

    for i in range(1, n + 1):
        print(*ans[i][1:])
