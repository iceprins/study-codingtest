import sys

INF = sys.maxsize


def bellman_ford(start):
    dist[start] = 0
    for i in range(N):
        for j in range(M):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            if dist[cur_node] != INF and dist[next_node] > dist[cur_node] + edge_cost:
                dist[next_node] = dist[cur_node] + edge_cost
                if i == N - 1:
                    return True

    return False


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    edges = []
    dist = [INF] * (N + 1)

    for _ in range(M):
        A, B, C = map(int, sys.stdin.readline().strip().split())
        edges.append((A, B, C))

    negative_cycle = bellman_ford(1)

    if negative_cycle:
        print(-1)
    else:
        for i in range(2, N + 1):
            if dist[i] == INF:
                print(-1)
            else:
                print(dist[i])
