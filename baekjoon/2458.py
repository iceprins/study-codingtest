import sys


def floyd_warshall():
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if height[i][j] == 1 or (height[i][k] == 1 and height[k][j] == 1):
                    height[i][j] = 1


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    height = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())
        height[a][b] = 1

    floyd_warshall()

    print(height)

    ans = 0

    for i in range(1, N + 1):
        known_height = 0
        for j in range(1, N + 1):
            known_height += height[i][j] + height[j][i]
        if known_height == N - 1:
            ans += 1

    print(ans)
