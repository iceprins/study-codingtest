import sys

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

if __name__ == '__main__':
    N, M, K = map(int, sys.stdin.readline().strip().split())
    board = [[[] for _ in range(N)] for _ in range(N)]
    fireballs = []

    for _ in range(M):
        r, c, m, s, d = map(int, sys.stdin.readline().strip().split())
        fireballs.append([r - 1, c - 1, m, s, d])

    for _ in range(K):
        while fireballs:
            r, c, m, s, d = fireballs.pop()
            nr = (r + s * dx[d]) % N
            nc = (c + s * dy[d]) % N
            board[nr][nc].append([m, s, d])

        for i in range(N):
            for j in range(N):
                if len(board[i][j]) > 1:
                    sm, ss, odd, even, cnt = 0, 0, 0, 0, len(board[i][j])
                    while board[i][j]:
                        m, s, d = board[i][j].pop(0)
                        sm += m
                        ss += s
                        if d % 2 == 0:
                            even += 1
                        else:
                            odd += 1
                    if odd == cnt or even == cnt:
                        nd = [0, 2, 4, 6]
                    else:
                        nd = [1, 3, 5, 7]

                    if sm // 5 != 0:
                        for d in nd:
                            fireballs.append([i, j, sm // 5, ss // cnt, d])

                if len(board[i][j]) == 1:
                    fireballs.append([i, j] + board[i][j].pop())

    print(sum(f[2] for f in fireballs))
