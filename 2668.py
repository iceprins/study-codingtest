import sys


N = int(sys.stdin.readline().strip())
table = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
result = list()

for i in range(1, N + 1):
    table[int(sys.stdin.readline().strip())].append(i)


def dfs(v):
    visited[v] = True
    for i in table[v]:
        if visited[i]:
            result.append(i)
        if not visited[i]:
            dfs(i)


if __name__ == '__main__':
    for i in range(1, N + 1):
        dfs(i)
        visited = [False] * (N + 1)

    print(len(result))
    for elem in result:
        print(elem)