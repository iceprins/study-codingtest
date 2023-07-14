import sys
from collections import deque

computers, relations = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(computers + 1)]
result = list()

for _ in range(relations):
    node, linked = map(int, sys.stdin.readline().strip().split())
    if node not in graph[linked]:
        graph[linked].append(node)


def bfs(graph, start):
    queue = deque([start])
    visited = [False] * (computers + 1)
    visited[start] = True
    cnt = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1

    return cnt


if __name__ == '__main__':
    max_val = -1
    for i in range(1, computers+1):
        temp = bfs(graph, i)
        if temp > max_val:
            max_val = temp
        result.append(temp)

    for i in range(computers):
        if max_val == result[i]:
            print(i+1, end=' ')