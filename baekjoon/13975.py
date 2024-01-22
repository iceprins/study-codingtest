import sys
import heapq

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        K = int(sys.stdin.readline().strip())
        chapter = list(map(int, sys.stdin.readline().strip().split()))

        chapter.sort()

        ans = 0

        while len(chapter) != 1:
            a = heapq.heappop(chapter)
            b = heapq.heappop(chapter)
            ans += (a + b)
            heapq.heappush(chapter, a + b)

        print(ans)
