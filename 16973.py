import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def is_wall(r, c):
    for r_wall, c_wall in walls:
        if r <= r_wall < r + h and c <= c_wall < c + w:
            return False
    return True


def bfs():
    queue = deque()
    queue.append((dep_r - 1, dep_c - 1, 0))

    while queue:
        y, x, cnt = queue.popleft()
        visited[y][x] = True

        if y == ar_r - 1 and x == ar_c - 1:
            print(cnt)
            return

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < column and 0 <= new_y < row and 0 <= new_x + w - 1 < column and 0 <= new_y + h - 1 < row:
                if not visited[new_y][new_x]:
                    if is_wall(new_y, new_x):
                        visited[new_y][new_x] = True
                        queue.append((new_y, new_x, cnt + 1))

    print(-1)
    return


if __name__ == '__main__':
    row, column = map(int, sys.stdin.readline().strip().split())
    board = list()

    for _ in range(row):
        board.append(list(map(int, sys.stdin.readline().strip().split())))

    h, w, dep_r, dep_c, ar_r, ar_c = map(int, sys.stdin.readline().strip().split())

    visited = [[False] * column for _ in range(row)]

    walls = list()
    for i in range(row):
        for j in range(column):
            if board[i][j] == 1:
                walls.append((i, j))

    bfs()