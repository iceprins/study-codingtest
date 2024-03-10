import sys


def dfs(vertex, cnt):
    cnt += 1
    visited[vertex] = True

    if vertex == target_2:
        ans.append(cnt)

    for i in family[vertex]:
        if not visited[i]:
            dfs(i, cnt)


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    target_1, target_2 = map(int, sys.stdin.readline().strip().split())
    m = int(sys.stdin.readline().strip())
    family = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for i in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())
        family[a].append(b)
        family[b].append(a)

    ans = []

    dfs(target_1, 0)

    if len(ans) == 0:
        print(-1)
    else:
        print(ans[0] - 1)
