if __name__ == '__main__':
    N = int(input())
    ans = 0

    while N >= 3 and N % 5 != 0:
        N -= 3
        ans += 1

    if 0 < N < 5 or N % 5 != 0:
        print(-1)
    elif N == 0:
        print(ans)
    else:
        print(ans + N // 5)
