if __name__ == '__main__':
    A, B = map(int, input().strip().split())
    cnt = 0

    while True:
        if A == B:
            break
        if (B % 2 != 0 and B % 10 != 1) or A > B:
            cnt = -2
            break
        if B % 2 == 1:
            B //= 10
            cnt += 1
            continue
        B >>= 1
        cnt += 1

    print(cnt + 1)