import sys
from collections import deque


def dfs(depth, idx):
    global result
    chicken_dist = 0

    if depth == M:
        for h in house:
            hx, hy = h[0], h[1]
            dist = sys.maxsize
            for c in selected:
                cx, cy = c[0], c[1]
                tmp = abs(hx - cx) + abs(hy - cy)
                dist = min(dist, tmp)
            chicken_dist += dist

        result = min(result, chicken_dist)

        return

    for i in range(idx, K):
        selected.append(chicken[i])
        dfs(depth + 1, idx + 1)
        selected.pop()

    return


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    house = deque()
    chicken = deque()
    selected = deque()

    for i in range(N):
        row = list(map(int, sys.stdin.readline().strip().split()))
        for j in range(N):
            if row[j] == 1:
                house.append((i, j))
            elif row[j] == 2:
                chicken.append((i, j))

    K = len(chicken)
    result = sys.maxsize

    for i in range(K):
        dfs(0, i)

    print(result)
