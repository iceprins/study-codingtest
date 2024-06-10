import sys

if __name__ == '__main__':
    V, E = map(int, sys.stdin.readline().strip().split())
    graph = [[sys.maxsize for _ in range(V + 1)] for _ in range(V + 1)]

    for _ in range(E):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        graph[a][b] = c

    for k in range(1, V + 1):
        for i in range(1, V + 1):
            for j in range(1, V + 1):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    ans = sys.maxsize

    for i in range(1, V + 1):
        ans = min(ans, graph[i][i])

    if ans == sys.maxsize:
        print(-1)
    else:
        print(ans)
