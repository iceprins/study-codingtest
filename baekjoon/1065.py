if __name__ == '__main__':
    N = int(input())
    ans = 0

    if N < 100:
        ans = N
    else:
        for num in range(100, N + 1):
            tmp = list(map(int, str(num)))
            a, b, c = tmp[0], tmp[1], tmp[2]
            if 2 * b == a + c:
                ans += 1
        ans += 99

    print(ans)
