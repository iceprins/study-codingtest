import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


def dfs(node):
    visited[node] = True
    children = []

    for child in graph[node]:
        if not visited[child]:
            children.append(child)
            dfs(child)

    dp[node][0] = 0
    dp[node][1] = residents[node]

    for child in children:
        dp[node][0] += max(dp[child][0], dp[child][1])
        dp[node][1] += dp[child][0]

    return


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    residents = list(map(int, sys.stdin.readline().strip().split()))
    graph = defaultdict(list)
    dp = [[0] * 2 for _ in range(N)]
    visited = [False] * N

    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    dfs(0)

    print(max(dp[0]))
