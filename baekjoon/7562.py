import sys
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(x, y, v):
    if x == x2 and y == y2:
        return 0
    queue = deque()
    queue.append((x, y))
    v[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > board_size - 1 or ny < 0 or ny > board_size - 1:
                continue
            if nx == x2 and ny == y2:
                return v[x][y]

            if v[nx][ny] == 0:
                v[nx][ny] = v[x][y] + 1
                queue.append((nx, ny))


if __name__ == '__main__':
    testcase = int(sys.stdin.readline().strip())

    for _ in range(testcase):
        board_size = int(sys.stdin.readline().strip())
        x1, y1 = map(int, sys.stdin.readline().strip().split())
        x2, y2 = map(int, sys.stdin.readline().strip().split())

        visited = [[0 for _ in range(board_size)] for _ in range(board_size)]

        ans = bfs(x1, y1, visited)

        print(ans)
