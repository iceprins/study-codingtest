import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()
    melt = deque()
    queue.append((0, 0))
    visited[0][0] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < row and 0 <= ny < column and not visited[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] == 0:
                    queue.append((nx, ny))
                elif board[nx][ny] == 1:
                    melt.append((nx, ny))

    for i in melt:
        x, y = i[0], i[1]
        board[x][y] = 0
    return len(melt)


if __name__ == '__main__':
    row, column = map(int, sys.stdin.readline().strip().split())
    board = list()
    remaining_area = 0
    cnt = 0

    for i in range(row):
        board.append(list(map(int, sys.stdin.readline().strip().split())))
        cnt += sum(board[i])

    spend_time = 0
    while True:
        visited = [[False for _ in range(column)] for _ in range(row)]
        melt_cnt = bfs()
        cnt -= melt_cnt
        spend_time += 1

        if cnt == 0:
            print(spend_time)
            print(melt_cnt)
            break