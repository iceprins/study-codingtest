import sys
from collections import deque

def bfs(g, start, v):
    queue = deque()
    queue.append(start)
    v[start] = True
    while queue:
        now = queue.popleft()
        for i in g[now]:
            if not v[i]:
                queue.append(i)
                v[i] = True

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    graph = [[i] for i in range(N + 1)]
    visited = [False] * (N + 1)
    sol = list()

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0

    for i in range(1, N + 1):
        if not visited[i]:
            bfs(graph, i, visited)
            cnt += 1

    print(cnt)