import sys
from collections import deque

vertex, edge, start_node = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(vertex + 1)]

for _ in range(edge):
    node, linked = map(int, sys.stdin.readline().strip().split())
    if node not in graph[linked]:
        graph[linked].append(node)
        graph[linked].sort()
    if linked not in graph[node]:
        graph[node].append(linked)
        graph[node].sort()

visited_dfs = [False] * (vertex + 1)
visited_bfs = [False] * (vertex + 1)


def dfs(graph, v, visited_dfs):
    visited_dfs[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)


def bfs(graph, start, visited_bfs):
    queue = deque([start])
    visited_bfs[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True


if __name__ == '__main__':
    dfs(graph, start_node, visited_dfs)
    print()
    bfs(graph, start_node, visited_bfs)