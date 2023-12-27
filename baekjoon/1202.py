import sys
import heapq

jewel_num, bag_num = map(int, sys.stdin.readline().split())

jewels = list()
max_weight = list()
temp = list()

for _ in range(jewel_num):
    heapq.heappush(jewels, tuple(map(int, sys.stdin.readline().split())))

for _ in range(bag_num):
    max_weight.append(int(sys.stdin.readline()))

max_weight.sort()
result = 0

for elem in max_weight:
    while jewels and elem >= jewels[0][0]:
        heapq.heappush(temp, -heapq.heappop(jewels)[1])
    if temp:
        result += -heapq.heappop(temp)
    elif not jewels:
        break

print(result)
