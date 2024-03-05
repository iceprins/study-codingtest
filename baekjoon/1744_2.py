import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    positive = list()
    negative = list()
    ans = 0

    for _ in range(N):
        num = int(sys.stdin.readline().strip())
        if num > 1:
            positive.append(num)
        elif num <= 0:
            negative.append(num)
        else:
            ans += num

    positive.sort(reverse=True)
    negative.sort()

    for i in range(0, len(positive), 2):
        if i + 1 < len(positive):
            ans += positive[i] * positive[i + 1]
        else:
            ans += positive[i]

    for i in range(0, len(negative), 2):
        if i + 1 < len(negative):
            ans += negative[i] * negative[i + 1]
        else:
            ans += negative[i]

    print(ans)
