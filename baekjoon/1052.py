if __name__ == '__main__':
    N, K = map(int, input().split())

    cnt = 0

    while bin(N).count('1') > K:
        idx = bin(N)[::-1].index('1')
        N += 2 ** idx
        cnt += 2 ** idx

    print(cnt)