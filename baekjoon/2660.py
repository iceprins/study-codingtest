# BFS 풀이
import sys
from collections import deque


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        now = q.popleft()
        for i in relationship[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                dist[i] = dist[now] + 1


if __name__ == '__main__':
    member = int(sys.stdin.readline().strip())
    relationship = [[] for _ in range(member + 1)]
    scores = [sys.maxsize] * (member + 1)

    while True:
        a, b = map(int, sys.stdin.readline().strip().split())

        if a == -1 and b == -1:
            break

        relationship[a].append(b)
        relationship[b].append(a)

    for i in range(1, member + 1):
        dist = [0] * (member + 1)
        visited = [False] * (member + 1)

        bfs(i)

        scores[i] = max(dist)

    chairman = []

    for i in range(member + 1):
        if scores[i] == min(scores):
            chairman.append(i)

    print(min(scores), len(chairman))
    print(*chairman)


# 플로이드-워셜
import sys

if __name__ == '__main__':
    member = int(sys.stdin.readline().strip())
    relationship = [[sys.maxsize for _ in range(member + 1)] for _ in range(member + 1)]

    while True:
        a, b = map(int, sys.stdin.readline().strip().split())

        if a == -1 and b == -1:
            break

        relationship[a][b] = 1
        relationship[b][a] = 1

    for i in range(1, member + 1):
        relationship[i][i] = 0

    for k in range(1, member + 1):
        for i in range(1, member + 1):
            for j in range(1, member + 1):
                if relationship[i][j] == 1 or relationship[i][j] == 0:
                    continue
                if relationship[i][j] > relationship[i][k] + relationship[k][j]:
                    relationship[i][j] = relationship[i][k] + relationship[k][j]

    scores = []

    for i in range(1, member + 1):
        scores.append(max(relationship[i][1:]))

    min_score = min(scores)

    print(min_score, scores.count(min_score))

    for idx, score in enumerate(scores):
        if score == min_score:
            print(idx + 1, end=' ')
