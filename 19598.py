import sys
import heapq

if __name__ == '__main__':
    meeting = int(sys.stdin.readline().strip())
    meeting_schedule = list()

    for _ in range(meeting):
        heapq.heappush(meeting_schedule, list(map(int, sys.stdin.readline().strip().split())))

    end_time = list()
    while meeting_schedule:
        min_room = heapq.heappop(meeting_schedule)

        if end_time:
            if min_room[0] >= end_time[0]:
                heapq.heappop(end_time)
        heapq.heappush(end_time, min_room[1])

    print(len(end_time))
