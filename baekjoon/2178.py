import sys
from collections import deque

rows, columns = map(int, sys.stdin.readline().strip().split())
maze = [[0 for _ in range(columns)] for _ in range(rows)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(v, w):
    queue = deque()
    queue.append((v, w))
    while queue:
        v, w = queue.popleft()
        for i in range(4):
            x = v + dx[i]
            y = w + dy[i]

            if x < 0 or y < 0 or x >= rows or y >= columns:
                continue
            if maze[x][y] == 0:
                continue
            if maze[x][y] == 1:
                maze[x][y] = maze[v][w] + 1
                queue.append((x, y))

    return maze[rows-1][columns-1]


if __name__ == '__main__':

    for i in range(rows):
        temp = list(sys.stdin.readline().strip())
        for j in range(columns):
            maze[i][j] = int(temp.pop(0))

    print(bfs(0, 0))