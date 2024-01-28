import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    cards = list(map(int, sys.stdin.readline().strip().split()))
    cand = list()

    cards.sort(reverse=True)

    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                cand.append(cards[i] + cards[j] + cards[k])

    cand.sort(reverse=True)

    for elem in cand:
        if elem <= M:
            print(elem)
            break
