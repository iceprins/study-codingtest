import sys
from collections import deque


def bfs():
    q = deque()
    q.append((home_x, home_y))
    while q:
        x, y = q.popleft()
        if abs(x - fest_x) + abs(y - fest_y) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = store[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    visited[i] = 1
                    q.append((nx, ny))
    print("sad")
    return


if __name__ == '__main__':
    t = int(sys.stdin.readline().strip())

    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        home_x, home_y = map(int, sys.stdin.readline().strip().split())
        store = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
        fest_x, fest_y = map(int, sys.stdin.readline().strip().split())
        visited = [0 for _ in range(n + 1)]

        bfs()
