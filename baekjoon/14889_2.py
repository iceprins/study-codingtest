import sys


def solve(n):
    global diff
    if len(ans) == N // 2:
        team_1, team_2 = 0, 0
        for i in ans:
            for j in ans:
                team_1 += S[i][j]

        tmp = list(set([i for i in range(N)]) - set(ans))

        for i in tmp:
            for j in tmp:
                team_2 += S[i][j]

        diff = min(diff, abs(team_1 - team_2))

        return

    for i in range(n, N):
        if i not in ans:
            ans.append(i)
            solve(i)
            ans.pop()


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    S = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    ans = []
    diff = sys.maxsize

    solve(0)

    print(diff)
