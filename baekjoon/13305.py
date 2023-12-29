import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    load_length = list(map(int, sys.stdin.readline().strip().split()))
    oil_price = list(map(int, sys.stdin.readline().strip().split()))

    ans = 0
    min_price = oil_price[0]
    for i in range(1, N):
        ans += min_price * load_length[i - 1]
        if oil_price[i] <= min_price:
            min_price = oil_price[i]

    print(ans)