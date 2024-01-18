import sys

sys.setrecursionlimit(10 ** 6)


def dfs(depart, weight):
    for i in edges[depart]:
        new_depart, new_weight = i
        if distance[new_depart] == -1:
            distance[new_depart] = weight + new_weight
            dfs(new_depart, weight + new_weight)


if __name__ == '__main__':
    node = int(sys.stdin.readline().strip())
    edges = [[] for _ in range(node + 1)]
    visited = [False] * (node + 1)

    for _ in range(node - 1):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        edges[a].append((b, c))
        edges[b].append((a, c))

    distance = [-1] * (node + 1)
    distance[1] = 0
    dfs(1, 0)

    start = distance.index(max(distance))

    distance = [-1] * (node + 1)
    distance[start] = 0
    dfs(start, 0)

    print(max(distance))
