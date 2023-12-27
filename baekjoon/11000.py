import sys
import heapq

if __name__ == '__main__':
    lecture_cnt = int(sys.stdin.readline().strip())

    lecture_plan = list()
    for _ in range(lecture_cnt):
        heapq.heappush(lecture_plan, list(map(int, sys.stdin.readline().strip().split())))

    end_time = list()
    while lecture_plan:  # lecture의 데이터가 더 이상 없을 때까지 반복
        min_lec = heapq.heappop(lecture_plan)

        if end_time:    # end_time의 데이터가 존재하면
            if min_lec[0] >= end_time[0]:
                heapq.heappop(end_time)
        heapq.heappush(end_time, min_lec[1])

    print(len(end_time))
    