import sys
import heapq

pair_num = int(sys.stdin.readline().strip())
pairs = list()
result = 0

for _ in range(pair_num):
    heapq.heappush(pairs, int(sys.stdin.readline().strip()))

if len(pairs) == 1:
    print(0)
else:
    while len(pairs) > 1:
        temp = heapq.heappop(pairs) + heapq.heappop(pairs)
        result += temp
        heapq.heappush(pairs, temp)

    print(result)
