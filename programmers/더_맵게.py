import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        first_val = heapq.heappop(scoville)

        if first_val >= K:
            break

        if not scoville:
            answer = -1
            break

        second_val = heapq.heappop(scoville)

        new_val = first_val + second_val * 2
        heapq.heappush(scoville, new_val)

        answer += 1

    return answer
