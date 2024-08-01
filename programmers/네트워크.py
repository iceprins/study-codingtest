# union-find 풀이
def union(x, y, p):
    x = find(x, p)
    y = find(y, p)

    if x < y:
        p[y] = x
    else:
        p[x] = y


def find(x, p):
    if x != p[x]:
        p[x] = find(p[x], p)
    return p[x]


def solution(n, computers):
    parents = [i for i in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if i != j and computers[i][j] == 1:
                union(i, j, parents)

    ans = set()

    for i in range(n):
        ans.add(find(i, parents))

    return len(ans)


# DFS 풀이
def dfs(n, computers, start, visited):
    visited[start] = True
    for i in range(n):
        if i != start and computers[start][i] == 1:
            if not visited[i]:
                dfs(n, computers, i, visited)


def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs(n, computers, i, visited)
            answer += 1

    return answer
