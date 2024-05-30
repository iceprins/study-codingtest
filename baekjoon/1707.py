import sys

sys.setrecursionlimit(10 ** 6)


def dfs(start, group):
    visited[start] = group

    for v in graph[start]:
        if visited[v] == 0:
            result = dfs(v, -group)
            if not result:
                return False
        else:
            if visited[v] == group:
                return False

    return True


if __name__ == '__main__':
    K = int(sys.stdin.readline().strip())

    for _ in range(K):
        V, E = map(int, sys.stdin.readline().strip().split())
        graph = [[] for _ in range(V + 1)]
        visited = [0] * (V + 1)

        for _ in range(E):
            a, b = map(int, sys.stdin.readline().strip().split())
            graph[a].append(b)
            graph[b].append(a)

        for i in range(1, V + 1):
            if visited[i] == 0:
                result = dfs(i, 1)
                if not result:
                    print("NO")
                    break
        else:
            print("YES")
