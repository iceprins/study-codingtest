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
    dp[node][1] = 1

    for child in children:
        dp[node][0] += dp[child][1]
        dp[node][1] += min(dp[child])

    return


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    graph = defaultdict(list)
    dp = [[0] * 2 for _ in range(N)]
    visited = [False] * N

    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    dfs(0)

    print(min(dp[0]))
