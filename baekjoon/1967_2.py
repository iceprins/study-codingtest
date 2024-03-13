import sys

sys.setrecursionlimit(10 ** 6)


def dfs(node, weight):
    for i in edge[node]:
        a, b = i
        if distance[a] == -1:
            distance[a] = b + weight
            dfs(a, b + weight)


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    edge = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        edge[a].append([b, c])
        edge[b].append([a, c])

    distance = [-1 for _ in range(n + 1)]
    distance[1] = 0
    dfs(1, 0)

    start = distance.index(max(distance))

    distance = [-1 for _ in range(n + 1)]
    distance[start] = 0
    dfs(start, 0)

    print(max(distance))
