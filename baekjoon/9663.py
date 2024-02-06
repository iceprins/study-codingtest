def promising(row):
    for i in range(row):
        if board[i] == board[row] or abs(board[i] - board[row]) == abs(i - row):
            return False
    return True


def dfs(row):
    global ans
    if row == N:
        ans += 1
    else:
        for i in range(N):
            board[row] = i
            if promising(row):
                dfs(row + 1)


if __name__ == '__main__':
    N = int(input())
    board = [0] * N
    ans = 0

    dfs(0)

    print(ans)
