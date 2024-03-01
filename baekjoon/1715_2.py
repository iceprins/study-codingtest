import sys
import heapq

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    cards = list(int(sys.stdin.readline().strip()) for _ in range(N))

    cards.sort()
    cnt = 0

    while len(cards) != 1:
        first = heapq.heappop(cards)
        second = heapq.heappop(cards)

        new = first + second

        heapq.heappush(cards, new)
        cnt += new

    print(cnt)
