import sys

N = int(sys.stdin.readline().strip())
goal = int(sys.stdin.readline().strip())

arr = [[0] * N for _ in range(N)]
ans = [N//2 + 1] * 2

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def sol():
    x, y = N // 2, N // 2
    arr[x][y] = 1

    x -= 1
    y -= 1

    num = 2
    iter_len = 2
    p = 0

    while True:
        for _ in range(4):
            x_d, y_d = dx[p], dy[p]
            for _ in range(iter_len):
                x += x_d
                y += y_d
                arr[y][x] = num
                if num == goal:
                    ans[0] = x + 1
                    ans[1] = y + 1
                if num == N ** 2:
                    return
                num += 1
            p = (p + 1) % 4
        iter_len += 2
        x -= 1
        y -= 1


if __name__ == '__main__':
    sol()

    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()

    print(ans[1], ans[0])