import sys
from collections import deque

board = list()
queue = deque()
dx = [0, -1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 0, -1, 1, -1, 1, -1, 1]


def move_wall():
    for i in range(7):
        board[7-i] = board[6-i]
    board[0] = ['.', '.', '.', '.', '.', '.', '.', '.']
    return


def bfs():
    queue.append((7, 0))
    cnt = 0
    while queue:
        len_q = len(queue)
        for _ in range(len_q):
            x, y = queue.popleft()
            if (x, y) == (0, 7):
                return 1
            if board[x][y] == '#':
                continue
            for i in range(9):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0 <= nx < 8 and 0 <= ny < 8):
                    continue
                if board[nx][ny] == '.':
                    queue.append((nx, ny))
        move_wall()
        cnt += 1
        if cnt == 9:
            return 1
    return 0


if __name__ == '__main__':
    for i in range(8):
        board.append(list(sys.stdin.readline().strip()))

    print(bfs())