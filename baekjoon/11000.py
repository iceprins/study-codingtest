import sys
import heapq

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    lessons = list()
    room = list()

    for _ in range(N):
        lessons.append(tuple(map(int, sys.stdin.readline().strip().split())))

    lessons.sort(key=lambda x: (x[0], x[1]))
    heapq.heappush(room, lessons[0][1])

    for i in range(1, N):
        if lessons[i][0] >= room[0]:
            heapq.heappop(room)
            heapq.heappush(room, lessons[i][1])
        else:
            heapq.heappush(room, lessons[i][1])

    print(len(room))