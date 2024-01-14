import sys

def dfs(g, start, v, cnt):
    cnt += 1
    v[start] = True

    if start == second:
        ans.append(cnt)

    for i in g[start]:
        if not v[i]:
            dfs(g, i, v, cnt)

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    first, second = map(int, sys.stdin.readline().strip().split())
    m = int(sys.stdin.readline().strip())

    edges = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    ans = list()

    for i in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())
        edges[a].append(b)
        edges[b].append(a)

    dfs(edges, first, visited, 0)

    if len(ans) == 0:
        print(-1)
    else:
        print(ans[0] - 1)