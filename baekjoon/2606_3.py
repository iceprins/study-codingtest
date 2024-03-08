import sys
from collections import deque


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    cnt = 0

    while q:
        now = q.popleft()
        cand = graph[now]
        for i in cand:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1

    return cnt


""""
DFS로 푸는 경우

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
"""

if __name__ == '__main__':
    computers = int(sys.stdin.readline().strip())
    pairs = int(sys.stdin.readline().strip())
    graph = [[] for _ in range(computers + 1)]
    visited = [False] * (computers + 1)

    for _ in range(pairs):
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    print(bfs(1))
