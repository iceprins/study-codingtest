import sys


def dfs(g, s, v):
    global cnt
    if s == erase:
        return
    v[s] = True
    if len(g[s]) == 1 and erase in g[s]:
        cnt += 1
    if len(g[s]) == 0:
        cnt += 1
        return
    for node in g[s]:
        if not v[node]:
            dfs(g, node, v)


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    parents = list(map(int, sys.stdin.readline().strip().split()))
    erase = int(sys.stdin.readline().strip())

    graph = [[] for _ in range(N)]
    visited = [False] * N
    start = -1

    for i in range(N):
        if parents[i] == -1:
            start = i
            continue
        graph[parents[i]].append(i)

    cnt = 0

    dfs(graph, start, visited)

    print(cnt)
