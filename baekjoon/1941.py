import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(arr):
    visited = [[1] * 5 for _ in range(5)]

    for i in arr:
        visited[i[0]][i[1]] = 0

    q = deque()
    q.append(arr[0])
    visited[arr[0][0]][arr[0][1]] = 1
    check = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > 4 or ny < 0 or ny > 4:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                check += 1
                q.append((nx, ny))

    if check != 7:
        return False

    return True


def dfs(start, depth, cnt):
    global ans

    if cnt >= 4:
        return

    if depth == 7:
        if bfs(record):
            ans += 1
        return

    for i in range(start, 25):
        r = i // 5
        c = i % 5
        record.append((r, c))
        dfs(i + 1, depth + 1, cnt + (seat[r][c] == 'Y'))
        record.pop()


if __name__ == '__main__':
    seat = [list(sys.stdin.readline().strip()) for _ in range(5)]
    record = []
    ans = 0

    dfs(0, 0, 0)

    print(ans)
