import sys

sys.setrecursionlimit(10**6)

node = int(sys.stdin.readline().strip())
graph = [[] for _ in range(node + 1)]
visited = [False] * (node + 1)
parent = [0] * (node + 1)

for _ in range(node - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    if a not in graph[b]:
        graph[b].append(a)
        graph[b].sort()
    if b not in graph[a]:
        graph[a].append(b)
        graph[a].sort()


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            parent[i] = v
            dfs(graph, i, visited)


if __name__ == '__main__':
    dfs(graph, 1, visited)

    for elem in parent:
        if elem != 0:
            print(elem)