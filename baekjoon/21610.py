import sys
from collections import deque
from copy import deepcopy

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    clouds_old = deque([(N - 1, 0), (N - 1, 1), ((N - 2) % N, 0), ((N - 2) % N, 1)])

    for _ in range(M):
        d, s = map(int, sys.stdin.readline().strip().split())

        # 모든 구름 이동
        for _ in range(len(clouds_old)):
            x, y = clouds_old.popleft()
            nx = (x + s * dx[d - 1]) % N
            ny = (y + s * dy[d - 1]) % N
            clouds_old.append((nx, ny))

        # 구름에 비 내림
        for cloud in clouds_old:
            x, y = cloud
            A[x][y] += 1

        # 물 복사
        for cloud in clouds_old:
            x, y = cloud
            cnt = 0
            for i in (1, 3, 5, 7):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                    continue
                if A[nx][ny] != 0:
                    cnt += 1
            A[x][y] += cnt

        cloud_tmp = deepcopy(clouds_old)
        clouds_old.clear()

        # 구름 다시 생성
        for i in range(N):
            for j in range(N):
                if A[i][j] >= 2:
                    if (i, j) not in cloud_tmp:
                        clouds_old.append((i, j))
                        A[i][j] -= 2

        cloud_tmp.clear()

    result = 0

    for i in range(N):
        result += sum(A[i])

    print(result)
