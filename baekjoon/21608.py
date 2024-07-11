import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solve(arr):
    cand = []

    for i in range(N):
        for j in range(N):
            if seat[i][j] == 0:
                prefer, empty = 0, 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                        continue
                    if seat[nx][ny] in arr[1:]:
                        prefer += 1
                    if seat[nx][ny] == 0:
                        empty += 1

                cand.append((i, j, prefer, empty))

    cand.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
    seat[cand[0][0]][cand[0][1]] = arr[0]

    return


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    info = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N ** 2)]

    seat = [[0 for _ in range(N)] for _ in range(N)]

    for student in info:
        solve(student)

    info.sort()
    scores = [0, 1, 10, 100, 1000]
    ans = 0

    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                    continue
                if seat[nx][ny] in info[seat[i][j] - 1]:
                    cnt += 1

            ans += scores[cnt]

    print(ans)
