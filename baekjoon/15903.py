import sys
import heapq

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().strip().split())
    cards = list(map(int, sys.stdin.readline().strip().split()))

    cards.sort()

    for i in range(m):
        first = heapq.heappop(cards)
        second = heapq.heappop(cards)

        new = first + second
        first = new
        second = new

        heapq.heappush(cards, first)
        heapq.heappush(cards, second)

    print(sum(cards))