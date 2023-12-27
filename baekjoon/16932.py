import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
board = list()
queue = deque()
visited = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    cnt = 1
    queue.append((i, j))
    visited[i][j] = idx
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not (0 <= nx < N and 0 <= ny < M) or visited[nx][ny] != 0:
                continue
            if board[nx][ny] == 1:
                visited[nx][ny] = idx
                queue.append((nx, ny))
                cnt += 1
    return cnt


if __name__ == '__main__':
    for _ in range(N):
        board.append(list(map(int, sys.stdin.readline().strip().split())))

    idx = 1
    group = dict()
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and not visited[i][j]:
                cnt = bfs(i, j)
                group[idx] = cnt
                idx += 1

    result = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                s = set()
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if not (0 <= ni < N and 0 <= nj < M):
                        continue
                    if board[ni][nj] == 1 and visited[ni][nj] not in s:
                        s.add(visited[ni][nj])
                res = 1
                for ss in s:
                    res += group[ss]
                result = max(result, res)

    print(result)