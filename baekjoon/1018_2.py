import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(N)]
    ans = sys.maxsize

    for i in range(N - 7):
        for j in range(M - 7):
            cnt_white = 0
            cnt_black = 0
            for p in range(i, i + 8):
                for q in range(j, j + 8):
                    if (p + q) % 2 == 0:
                        if board[p][q] == 'W':
                            cnt_black += 1
                        else:
                            cnt_white += 1
                    else:
                        if board[p][q] == 'W':
                            cnt_white += 1
                        else:
                            cnt_black += 1

            ans = min(ans, cnt_white, cnt_black)

    print(ans)
