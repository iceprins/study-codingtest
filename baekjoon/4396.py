import sys

board_size = int(sys.stdin.readline().strip())
mine = list()
cond = list()

for _ in range(board_size):
    mine.append(list(sys.stdin.readline().strip()))

for _ in range(board_size):
    cond.append(list(sys.stdin.readline().strip()))


def mine_cnt(r, c):
    count = 0

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(8):
        trans_r = r + dx[i]
        trans_c = c + dy[i]
        if 0 <= trans_r < board_size and 0 <= trans_c < board_size:
            if mine[trans_r][trans_c] == '*':
                count += 1

    return count


def print_ans():
    for i in range(board_size):
        for j in range(board_size):
            print(cond[i][j], end='')
        print()


if __name__ == '__main__':
    check = False
    for i in range(board_size):
        for j in range(board_size):
            if cond[i][j] == 'x' and mine[i][j] == '*' and not check:
                check = True
            elif cond[i][j] == 'x' and mine[i][j] == '.':
                cond[i][j] = mine_cnt(i, j)
            else:
                cond[i][j] = '.'

    if check:
        for i in range(board_size):
            for j in range(board_size):
                if mine[i][j] == '*':
                    cond[i][j] = '*'

    print_ans()