import sys

sys.setrecursionlimit(10 ** 6)


def dfs(vertex):
    visited[vertex] = True
    for i in tree[vertex]:
        if not visited[i]:
            parents[i] = vertex
            dfs(i)


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    tree = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    parents = [0] * (N + 1)

    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().strip().split())
        tree[a].append(b)
        tree[b].append(a)

    dfs(1)

    for i in range(2, N + 1):
        print(parents[i])
