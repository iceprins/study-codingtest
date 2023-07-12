import sys

computers = int(sys.stdin.readline().strip())
pairs = int(sys.stdin.readline().strip())
graph = [[] for _ in range(computers + 1)]
visited = [False] * (computers + 1)
cnt = 0

for _ in range(pairs):
    computer, linked = map(int, sys.stdin.readline().strip().split())
    if linked not in graph[computer]:
        graph[computer].append(linked)
    if computer not in graph[linked]:
        graph[linked].append(computer)


def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


if __name__ == '__main__':
    dfs(graph, 1, visited)
    print(cnt - 1)