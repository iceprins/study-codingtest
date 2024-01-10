import sys
from collections import deque

def bfs(graph, start, visited, cnt):
    queue = deque([start])
    visited[start] = True
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1

    return cnt

if __name__ == '__main__':
    computer = int(sys.stdin.readline().strip())
    connected = int(sys.stdin.readline().strip())
    pairs = list([] for i in range(computer + 1))

    for _ in range(connected):
        a, b = map(int, sys.stdin.readline().strip().split())
        pairs[a].append(b)
        pairs[b].append(a)

    visited = [False] * (computer + 1)
    cnt = 1

    cnt = bfs(pairs, 1, visited, cnt)

    print(cnt - 1)