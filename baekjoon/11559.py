import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    target = board[x][y]
    cand = [(x, y)]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > 11 or ny < 0 or ny > 5:
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == target:
                visited[nx][ny] = True
                cand.append((nx, ny))
                q.append((nx, ny))

    if len(cand) >= 4:
        for elem in cand:
            board[elem[0]][elem[1]] = '.'
        return True
    else:
        return False


def down():
    for j in range(6):
        for i in range(10, -1, -1):
            for k in range(11, i, -1):
                if board[i][j] != "." and board[k][j] == ".":
                    board[k][j] = board[i][j]
                    board[i][j] = "."


if __name__ == '__main__':
    board = []
    cnt = 0

    for _ in range(12):
        board.append(list(sys.stdin.readline().strip()))

    while True:
        visited = [[False for _ in range(6)] for _ in range(12)]
        is_exploded = False

        for i in range(12):
            for j in range(6):
                if board[i][j] != '.' and not visited[i][j]:
                    result = bfs(i, j)
                    if result:
                        is_exploded = True

        if is_exploded:
            down()
            cnt += 1
        else:
            break

    print(cnt)
