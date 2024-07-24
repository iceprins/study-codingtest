import sys
import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra():
    q = []
    heapq.heappush(q, (cave[0][0], 0, 0))
    distance[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if x == N - 1 and y == N - 1:
            print(f"Problem {cnt}: {distance[x][y]}")
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            nc = cost + cave[nx][ny]

            if nc < distance[nx][ny]:
                distance[nx][ny] = nc
                heapq.heappush(q, (nc, nx, ny))


if __name__ == '__main__':
    cnt = 1

    while True:
        N = int(sys.stdin.readline().strip())

        if N == 0:
            break

        cave = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
        distance = [[sys.maxsize] * N for _ in range(N)]

        dijkstra()
        cnt += 1
