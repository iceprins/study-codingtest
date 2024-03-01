import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    words = list(sys.stdin.readline().strip() for _ in range(N))
    info = dict()

    for word in words:
        x = len(word) - 1
        for alpha in word:
            if alpha in info:
                info[alpha] += 10 ** x
            else:
                info[alpha] = 10 ** x
            x -= 1

    length = sorted(info.values(), reverse=True)

    ans = 0
    num = 9

    for i in length:
        ans += i * num
        num -= 1

    print(ans)
