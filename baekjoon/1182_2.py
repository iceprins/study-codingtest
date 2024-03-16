import sys


def solve(n):
    global cnt
    if sum(ans) == S and len(ans) > 0:
        cnt += 1

    for i in range(n, N):
        ans.append(sequence[i])
        solve(i + 1)
        ans.pop()


if __name__ == '__main__':
    N, S = map(int, sys.stdin.readline().strip().split())
    sequence = list(map(int, sys.stdin.readline().strip().split()))
    ans = []
    cnt = 0

    solve(0)

    print(cnt)
