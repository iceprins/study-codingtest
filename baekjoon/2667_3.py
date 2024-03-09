import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    board[x][y] = 0
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            if board[nx][ny] != 0:
                q.append((nx, ny))
                board[nx][ny] = 0
                cnt += 1

    return cnt


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    board = []

    for _ in range(N):
        board.append(list(map(int, sys.stdin.readline().strip())))

    house = []

    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                house.append(bfs(i, j))

    house.sort()

    print(len(house))

    for elem in house:
        print(elem)
