import sys

sys.setrecursionlimit(10 ** 6)


def dfs(v):
    cnt[v] = 1
    for i in graph[v]:
        if cnt[i] == 0:
            dfs(i)
            cnt[v] += cnt[i]


if __name__ == '__main__':
    N, R, Q = map(int, sys.stdin.readline().strip().split())
    cnt = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        U, V = map(int, sys.stdin.readline().strip().split())
        graph[U].append(V)
        graph[V].append(U)

    dfs(R)

    for _ in range(Q):
        U = int(sys.stdin.readline().strip())
        print(cnt[U])
