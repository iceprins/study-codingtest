import sys


def check(arr):
    visited = [False] * N
    for i in range(N - 1):
        if arr[i] == arr[i + 1]:
            continue
        elif abs(arr[i] - arr[i + 1]) > 1:
            return False
        elif arr[i] > arr[i + 1]:
            tmp = arr[i + 1]
            for j in range(i + 1, i + L + 1):
                if 0 <= j < N:
                    if tmp != arr[j]:
                        return False
                    elif visited[j]:
                        return False
                    visited[j] = True
                else:
                    return False
        else:
            tmp = arr[i]
            for j in range(i, i - L, -1):
                if 0 <= j < N:
                    if tmp != arr[j]:
                        return False
                    elif visited[j]:
                        return False
                    visited[j] = True
                else:
                    return False

    return True


if __name__ == '__main__':
    N, L = map(int, sys.stdin.readline().strip().split())
    board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    ans = 0

    for row in board:
        if check(row):
            ans += 1

    for i in range(N):
        col = []
        for j in range(N):
            col.append(board[j][i])
        if check(col):
            ans += 1

    print(ans)
