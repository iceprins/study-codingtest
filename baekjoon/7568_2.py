import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    info = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    ans = []

    for size in info:
        cnt = 0
        for i in range(N):
            if size[0] < info[i][0] and size[1] < info[i][1]:
                cnt += 1
        ans.append(cnt + 1)

    print(*ans)
