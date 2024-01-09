import sys
import heapq

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    pos_sequence = list()
    neg_sequence = list()

    for _ in range(N):
        num = int(sys.stdin.readline().strip())
        if num > 0:
            heapq.heappush(pos_sequence, -num)
        else:
            heapq.heappush(neg_sequence, num)

    result = 0

    while pos_sequence:
        if len(pos_sequence) == 1:
            result += - heapq.heappop(pos_sequence)
        else:
            first = - heapq.heappop(pos_sequence)
            second = - heapq.heappop(pos_sequence)
            result += first * second
            if second == 1:
                result += 1

    while neg_sequence:
        if len(neg_sequence) == 1:
            result += heapq.heappop(neg_sequence)
        else:
            first = heapq.heappop(neg_sequence)
            second = heapq.heappop(neg_sequence)
            result += first * second

    print(result)