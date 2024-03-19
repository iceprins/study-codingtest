import sys


def dfs(start, now, cost, cnt):
    global total
    if cnt == N:
        if costs[now][start] != 0:
            cost += costs[now][start]
            total = min(total, cost)
        return

    if cost > total:
        return

    for i in range(N):
        if costs[now][i] != 0 and not visited[i]:
            visited[i] = True
            dfs(start, i, cost + costs[now][i], cnt + 1)
            visited[i] = False


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    costs = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    visited = [False] * N

    total = sys.maxsize

    for i in range(N):
        visited[i] = True
        dfs(i, i, 0, 1)
        visited[i] = False

    print(total)
