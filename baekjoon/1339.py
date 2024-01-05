import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    words = list()
    calculate = dict()
    num = [i for i in range(0, 10)]
    ans = 0

    for _ in range(N):
        word = sys.stdin.readline().strip()
        words.append(word)
        for i in range(len(word), 0, -1):
            if word[-i] not in calculate:
                calculate[word[-i]] = 10 ** (i - 1)
            else:
                calculate[word[-i]] += 10 ** (i - 1)

    calculate = sorted(calculate.values(), reverse=True)

    for elem in calculate:
        ans += elem * num.pop()

    print(ans)