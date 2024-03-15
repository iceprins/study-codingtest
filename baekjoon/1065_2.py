if __name__ == '__main__':
    N = int(input())
    cnt = 0

    if N < 100:
        cnt = N
    else:
        cnt = 99
        for num in range(100, N + 1):
            tmp = list(map(int, str(num)))
            if tmp[1] * 2 == tmp[0] + tmp[2]:
                cnt += 1

    print(cnt)
