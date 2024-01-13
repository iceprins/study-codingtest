import sys
from collections import deque

# def dfs(g, start, v):


def bfs(g, start, v):
    result = -1
    queue = deque()
    queue.append(start)
    v[start] = True
    while queue:
        now = queue.popleft()
        for target in g[now]:
            if second == target:
                return result
            if not v[target]:
                queue.append(target)
                v[target] = True
                result += 1

    return -1

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    first, second = map(int, sys.stdin.readline().strip().split())
    m = int(sys.stdin.readline().strip())

    edges = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for i in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())
        edges[a].append(b)
        # edges[b].append(a)

    print(bfs(edges, first, visited))
    print(edges)