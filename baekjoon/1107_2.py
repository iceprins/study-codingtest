import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())
    broken = list(map(int, sys.stdin.readline().strip().split()))

    min_move = abs(N - 100)

    for num in range(1000001):
        num = str(num)

        for i in range(len(num)):
            if int(num[i]) in broken:
                break
            elif i == len(num) - 1:
                min_move = min(min_move, abs(int(num) - N) + len(num))

    print(min_move)
