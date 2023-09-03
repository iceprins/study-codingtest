import sys
from collections import deque

row, column = map(int, sys.stdin.readline().strip().split())
board = [list(map(str, sys.stdin.readline().strip())) for _ in range(row)]
human_queue = deque()
fire_queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

human = [[0] * column for _ in range(row)]
fire = [[0] * column for _ in range(row)]

for i in range(row):
    for j in range(column):
        if board[i][j] == "J":
            human_queue.append((i, j))
            human[i][j] = 1
        if board[i][j] == "F":
            fire_queue.append((i, j))
            fire[i][j] = 1


def fire_bfs():
    while fire_queue:
        x, y = fire_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < row and 0 <= ny < column):
                continue
            if board[nx][ny] == "#" or fire[nx][ny] != 0:
                continue
            fire[nx][ny] = fire[x][y] + 1
            fire_queue.append((nx, ny))


def human_bfs():
    while human_queue:
        x, y = human_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < row and 0 <= ny < column):
                print(human[x][y])
                return
            if board[nx][ny] == "#" or human[nx][ny] != 0:
                continue
            if human[x][y] + 1 >= fire[nx][ny] and fire[nx][ny] != 0:
                continue
            human[nx][ny] = human[x][y] + 1
            human_queue.append((nx, ny))
    print("IMPOSSIBLE")
    return


if __name__ == '__main__':
    fire_bfs()
    human_bfs()