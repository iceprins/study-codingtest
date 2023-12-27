import sys
from collections import deque


row, column, second = map(int, sys.stdin.readline().strip().split())
board = list()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(row):
    temp = list()
    board.append(list(sys.stdin.readline().strip()))

queue = deque()


def bfs(q, board):
    while q:
        x, y = q.popleft()
        board[x][y] = '.'
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < row and 0 <= ny < column and board[nx][ny] == 'O':
                board[nx][ny] = '.'


def simulate(t):
    global queue, board
    if t == 1:
        for i in range(row):
            for j in range(column):
                if board[i][j] == 'O':
                    queue.append((i, j))
    elif t % 2 == 1:
        bfs(queue, board)
        for i in range(row):
            for j in range(column):
                if board[i][j] == 'O':
                    queue.append((i, j))
    else:
        board = [['O'] * column for _ in range(row)]


if __name__ == '__main__':
    for i in range(1, second + 1):
        simulate(i)
    for i in board:
        print(''.join(i))