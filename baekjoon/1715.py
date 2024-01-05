import sys
import heapq

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    cards = list()

    for _ in range(N):
        cards.append(int(sys.stdin.readline().strip()))

    cards.sort()

    ans = 0
    for i in range(N - 1):
        calculate = heapq.heappop(cards)
        calculate += heapq.heappop(cards)
        ans += calculate
        heapq.heappush(cards, calculate)


    print(ans)