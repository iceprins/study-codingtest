# BFS 풀이
import sys
from collections import deque


def bfs(start, end):
    q = deque()
    q.append(start)
    visited[start - 1] = True
    while q:
        now = q.popleft()
        if now == end:
            return True
        for i in range(N):
            if connection[now - 1][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i + 1)


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())

    connection = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    plan = list(map(int, sys.stdin.readline().strip().split()))

    result = "YES"

    for i in range(M - 1):
        visited = [False] * N
        flag = bfs(plan[i], plan[i + 1])
        if not flag:
            result = "NO"
            break

    print(result)


# Union-Find 풀이
import sys


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())

    parents = [i for i in range(N)]

    for i in range(N):
        connection = list(map(int, sys.stdin.readline().strip().split()))
        for j in range(N):
            if connection[j] == 1:
                union(i, j)

    parents = [-1] + parents
    plan = list(map(int, sys.stdin.readline().strip().split()))
    start = parents[plan[0]]
    
    for i in range(1, M):
        if parents[plan[i]] != start:
            print("NO")
            break
    else:
        print("YES")
