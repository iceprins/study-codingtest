import sys
from collections import deque

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    graph = [[] for _ in range(N + 1)]
    in_degree = [0 for _ in range(N + 1)]

    q = deque()
    answer = []

    for _ in range(M):
        A, B = map(int, sys.stdin.readline().strip().split())
        graph[A].append(B)
        in_degree[B] += 1

    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        tmp = q.popleft()
        answer.append(tmp)
        for i in graph[tmp]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)

    print(*answer)
