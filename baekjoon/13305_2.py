import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    roads = list(map(int, sys.stdin.readline().strip().split()))
    prices = list(map(int, sys.stdin.readline().strip().split()))

    price = sys.maxsize
    total = 0

    for i in range(N - 1):
        price = min(price, prices[i])
        total += price * roads[i]

    print(total)
