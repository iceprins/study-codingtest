def solve():
    if decreasing:
        ans.append(int(''.join(map(str, decreasing))))

    for i in range(10):
        if len(decreasing) == 0 or decreasing[-1] > i:
            decreasing.append(i)
            solve()
            decreasing.pop()


if __name__ == '__main__':
    N = int(input())
    decreasing = []
    ans = []
    cnt = 0

    solve()
    ans.sort()

    if N >= len(ans):
        print(-1)
    else:
        print(ans[N])
