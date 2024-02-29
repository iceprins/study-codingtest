import sys
import heapq

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    lessons = list(tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N))

    lessons.sort(key=lambda x: x[0])

    q = list()
    heapq.heappush(q, lessons[0][1])

    for i in range(1, N):
        tmp = heapq.heappop(q)
        if lessons[i][0] >= tmp:
            heapq.heappush(q, lessons[i][1])
        else:
            heapq.heappush(q, tmp)
            heapq.heappush(q, lessons[i][1])

    print(len(q))
