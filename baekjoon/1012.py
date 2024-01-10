import sys
from collections import deque
sys.setrecursionlimit(1000000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > M - 1 or ny < 0 or ny > N - 1:
                continue
            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((nx, ny))

def dfs(graph, x, y):
    if x < 0 or x > M - 1 or y < 0 or y > N - 1:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(graph, x - 1, y)
        dfs(graph, x + 1, y)
        dfs(graph, x, y - 1)
        dfs(graph, x, y + 1)
        return True
    return False

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        M, N, K = map(int, sys.stdin.readline().strip().split())
        position = [[0 for _ in range(M)] for _ in range(N)]

        for _ in range(K):
            a, b = map(int, sys.stdin.readline().strip().split())
            position[b][a] = 1

        result = 0

        for i in range(M):
            for j in range(N):
                if position[j][i] == 1:
                    bfs(position, i, j)
                    result += 1

                """
                dfs를 사용하는 경우
                if dfs(position, i, j):
                    result += 1
                """

        print(result)