import copy
import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [1, 2, 3], [0, 2, 3], [0, 1, 3]],
    [[0, 1, 2, 3]]
]


def fill(board, direction, x, y):
    for i in direction:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                break
            if board[nx][ny] == 6:
                break
            if board[nx][ny] == 0:
                board[nx][ny] = -1


def dfs(depth, original):
    global ans
    if depth == len(cctv):
        cnt = 0
        for i in range(N):
            cnt += original[i].count(0)
        ans = min(ans, cnt)
        return

    tmp = copy.deepcopy(original)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        fill(tmp, i, x, y)
        dfs(depth + 1, tmp)
        tmp = copy.deepcopy(original)


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    office = []
    cctv = []

    for i in range(N):
        arr = list(map(int, sys.stdin.readline().strip().split()))
        office.append(arr)
        for j in range(M):
            if arr[j] in [1, 2, 3, 4, 5]:
                cctv.append([arr[j], i, j])

    ans = sys.maxsize

    dfs(0, office)

    print(ans)
