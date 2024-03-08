import sys

sys.setrecursionlimit(10 ** 6)


def dfs(vertex):
    visited[vertex] = True
    now = graph[vertex]
    for elem in now:
        if not visited[elem]:
            dfs(elem)


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)

    for i in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            cnt += 1

    print(cnt)
