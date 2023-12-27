import sys

sys.setrecursionlimit(10**9)
node = int(sys.stdin.readline().strip())
graph = [[] for _ in range(node + 1)]

for i in range(node - 1):
    input_val = sys.stdin.readline().strip().split()
    idx, vertex, weight = int(input_val[0]), int(input_val[1]), int(input_val[2])
    graph[idx].append([vertex, weight])
    graph[vertex].append([idx, weight])


def dfs(start, w):
    for i in graph[start]:
        a, b = i
        if dist[a] == -1:
            dist[a] = w + b
            dfs(a, w + b)


if __name__ == '__main__':
    dist = [-1] * (node + 1)
    dist[1] = 0
    dfs(1, 0)

    init = dist.index(max(dist))

    dist = [-1] * (node + 1)
    dist[init] = 0
    dfs(init, 0)

    print(max(dist))