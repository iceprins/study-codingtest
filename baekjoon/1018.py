import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    board = list()

    for _ in range(N):
        board.append(list(sys.stdin.readline().strip()))

    result = list()

    for i in range(N - 7):
        for j in range(M - 7):
            cnt = 0
            for p in range(i, i + 8):
                for q in range(j, j + 8):
                    if p % 2 == 0 and q % 2 == 0 and board[p][q] == 'B':
                        cnt += 1
                        continue
                    if p % 2 != 0 and q % 2 != 0 and board[p][q] == 'B':
                        cnt += 1
                        continue
                    if ((p % 2 != 0 and q % 2 == 0) or (p % 2 == 0 and q % 2 != 0)) and board[p][q] == 'W':
                        cnt += 1
                        continue

            result.append(cnt)

            cnt = 0
            for p in range(i, i + 8):
                for q in range(j, j + 8):
                    if p % 2 == 0 and q % 2 == 0 and board[p][q] == 'W':
                        cnt += 1
                        continue
                    if p % 2 != 0 and q % 2 != 0 and board[p][q] == 'W':
                        cnt += 1
                        continue
                    if ((p % 2 == 0 and q % 2 != 0) or (p % 2 != 0 and q % 2 == 0)) and board[p][q] == 'B':
                        cnt += 1
                        continue

            result.append(cnt)

    print(min(result))
