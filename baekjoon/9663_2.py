def back(x):
    global cnt
    if x == N:
        cnt += 1
        return
    for i in range(N):
        board[x] = i
        if is_promising(x):
            back(x + 1)


def is_promising(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[x] - board[i]) == abs(x - i):
            return False

    return True


if __name__ == '__main__':
    N = int(input())
    board = [0] * N
    cnt = 0

    back(0)

    print(cnt)
