import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > R - 1 or ny < 0 or ny > C - 1:
            continue
        if board[nx][ny] not in history:
            history.add(board[nx][ny])
            dfs(nx, ny, cnt + 1)
            history.remove(board[nx][ny])


if __name__ == '__main__':
    R, C = map(int, sys.stdin.readline().strip().split())
    board = list()
    history = set()

    for _ in range(R):
        board.append(list(sys.stdin.readline().strip()))

    ans = 0

    history.add(board[0][0])
    dfs(0, 0, 1)

    print(ans)
