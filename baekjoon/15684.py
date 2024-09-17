import sys


def check():
    for i in range(N):
        now = i
        for j in range(H):
            if ladder[j][now]:
                now += 1
            elif now > 0 and ladder[j][now - 1]:
                now -= 1
        if now != i:
            return False
    return True


def dfs(x, y, cnt):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    if cnt == 3 or ans <= cnt:
        return

    for i in range(x, H):
        if i == x:
            now = y
        else:
            now = 0

        for j in range(now, N - 1):
            if not ladder[i][j] and not ladder[i][j + 1]:
                if j > 0 and ladder[i][j - 1]:
                    continue
                ladder[i][j] = True
                dfs(i, j + 2, cnt + 1)
                ladder[i][j] = False


if __name__ == '__main__':
    N, M, H = map(int, sys.stdin.readline().strip().split())
    ladder = [[False] * N for _ in range(H)]

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())
        ladder[a - 1][b - 1] = True

    ans = 4
    dfs(0, 0, 0)

    print(ans if ans < 4 else -1)
