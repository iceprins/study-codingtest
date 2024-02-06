import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, num, cnt):
    global ans
    if cnt == 4:
        ans = max(ans, num)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
            continue
        if not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, num + paper[nx][ny], cnt + 1)
            visited[nx][ny] = False


def other(x, y):
    global ans
    for i in range(4):
        tmp = paper[x][y]
        for j in range(3):
            t = (i + j) % 4
            nx = x + dx[t]
            ny = y + dy[t]

            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                tmp = 0
                break
            tmp += paper[nx][ny]
        ans = max(ans, tmp)


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    visited = [[False for _ in range(M)] for _ in range(N)]
    paper = list()

    for _ in range(N):
        paper.append(list(map(int, sys.stdin.readline().strip().split())))

    ans = 0

    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(i, j, paper[i][j], 1)
            visited[i][j] = False
            other(i, j)

    print(ans)
