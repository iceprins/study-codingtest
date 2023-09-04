import sys
from collections import deque

K = int(sys.stdin.readline().strip())
input_val = sys.stdin.readline().strip().split()
W, H = int(input_val[0]), int(input_val[1])
board = list()
queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
hx = [-2, -2, -1, 1, 2, 2, -1, 1]
hy = [-1, 1, 2, 2, -1, 1, -2, -2]

# visited = [[0] * W for _ in range(H)]
visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]


def bfs():
    global K
    queue.append((0, 0, K, 0))
    visited[0][0][0] = True
    while queue:
        x, y, k, cnt = queue.popleft()
        if x == H - 1 and y == W - 1:
            # return visited[x][y]
            return cnt

        if k > 0:
            for i in range(8):
                hnx = x + hx[i]
                hny = y + hy[i]
                if not (0 <= hnx < H and 0 <= hny < W):
                    continue
                if board[hnx][hny] == 1:
                    continue
                if visited[hnx][hny][k - 1]:
                    continue
                visited[hnx][hny][k - 1] = True
                queue.append((hnx, hny, k - 1, cnt + 1))
                # K -= 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < H and 0 <= ny < W):
                continue
            if board[nx][ny] == 1:
                continue
            if visited[nx][ny][k]:
                continue
            visited[nx][ny][k] = True
            queue.append((nx, ny, k, cnt + 1))

    return -1


if __name__ == '__main__':
    for _ in range(H):
        board.append(list(map(int, sys.stdin.readline().strip().split())))

    # for i in range(H):
    #     for j in range(W):
    #         if board[i][j] == 1:
    #             visited[i][j] = -1

    print(bfs())