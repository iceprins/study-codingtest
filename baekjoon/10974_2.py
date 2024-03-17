def solve():
    if len(ans) == N:
        print(*ans)

    for i in range(1, N + 1):
        if i not in ans:
            ans.append(i)
            solve()
            ans.pop()


if __name__ == '__main__':
    N = int(input())
    ans = []

    solve()
