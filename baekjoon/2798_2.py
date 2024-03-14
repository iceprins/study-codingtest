import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    cards = list(map(int, sys.stdin.readline().strip().split()))

    cards.sort(reverse=True)
    ans = 0

    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            for k in range(j + 1, len(cards)):
                tmp = cards[i] + cards[j] + cards[k]
                if tmp <= M:
                    ans = max(ans, tmp)

    print(ans)
