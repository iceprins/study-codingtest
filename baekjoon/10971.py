import sys


def dfs(depth, x):
    global cost, ans
    if depth == N - 1:
        if W[x][0]:
            cost += W[x][0]
            ans = min(ans, cost)
            cost -= W[x][0]
        return

    for i in range(1, N):
        if not visited[i] and W[x][i]:
            visited[i] = True
            cost += W[x][i]
            dfs(depth + 1, i)
            visited[i] = False
            cost -= W[x][i]


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    W = list()

    for _ in range(N):
        W.append(list(map(int, sys.stdin.readline().strip().split())))

    visited = [False] * N
    cost = 0
    ans = sys.maxsize

    dfs(0, 0)

    print(ans)
