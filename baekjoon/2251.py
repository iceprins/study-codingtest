from collections import deque


def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))


def bfs():
    while q:
        x, y = q.popleft()
        z = C - x - y

        if x == 0:
            ans.append(z)

        water = min(x, B - y)
        pour(x - water, y + water)

        water = min(x, C - z)
        pour(x - water, y)

        water = min(y, C - z)
        pour(x, y - water)

        water = min(y, A - x)
        pour(x + water, y - water)

        water = min(z, A - x)
        pour(x + water, y)

        water = min(z, B - y)
        pour(x, y + water)


if __name__ == '__main__':
    A, B, C = map(int, input().split())
    visited = [[False] * (B + 1) for _ in range(A + 1)]
    visited[0][0] = True

    q = deque()
    q.append((0, 0))

    ans = []

    bfs()

    ans.sort()

    print(*ans)
