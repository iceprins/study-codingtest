import sys
from collections import deque

row, column = map(int, sys.stdin.readline().strip().split())
board = list()
glacier = list()
queue = deque()

for _ in range(row):
    board.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(row):
    for j in range(column):
        if board[i][j] != 0:
            glacier.append((i, j))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs(x, y):
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < column:
                if board[nx][ny] == 0:
                    temp[x][y] += 1
                elif board[nx][ny] != 0 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    return 1


if __name__ == '__main__':
    ans = 0
    while True:
        visited = [[False] * column for _ in range(row)]
        temp = [[0] * column for _ in range(row)]
        result = list()
        # check = False

        for i in range(row):
            for j in range(column):
                if board[i][j] != 0 and not visited[i][j]:
                    result.append(bfs(i, j))

        for i in range(row):
            for j in range(column):
                board[i][j] -= temp[i][j]
                if board[i][j] < 0:
                    board[i][j] = 0

        if len(result) == 0:
            print(0)
            break
        if len(result) >= 2:
            print(ans)
            # check = True
            break

        ans += 1

    # if check:
    #     print(ans)
    # else:
    #     print(0)
