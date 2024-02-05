import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())
    broken = list(map(int, sys.stdin.readline().strip().split()))

    ans = abs(100 - N)

    for num in range(1000001):
        num = str(num)

        for i in range(len(num)):
            if int(num[i]) in broken:
                break

            elif i == len(num) - 1:
                ans = min(ans, abs(int(num) - N) + len(num))

    print(ans)
