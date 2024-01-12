import sys
from collections import deque
# sys.setrecursionlimit(10**6)

"""
dfs를 사용하는 경우

def dfs(g, v, visited):
    visited[v] = True
    for i in g[v]:
        if not visited[i]:
            history[i] = v
            dfs(g, i, visited)
"""

def bfs(g, start, v):
    queue = deque()
    queue.append(start)
    v[start] = True
    while queue:
        now = queue.popleft()
        for i in g[now]:
            if not v[i]:
                v[i] = True
                history[i] = now
                queue.append(i)

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    edges = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    history = [0] * (N + 1)

    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().strip().split())
        edges[a].append(b)
        edges[b].append(a)

    # dfs(edges, 1, visited)
    bfs(edges, 1, visited)

    for i in range(2, N + 1):
        print(history[i])