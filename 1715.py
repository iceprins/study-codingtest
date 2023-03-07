import sys
from queue import PriorityQueue

pair_num = int(sys.stdin.readline().strip())
pairs = PriorityQueue()
result = 0

for _ in range(pair_num):
    pairs.put(int(sys.stdin.readline().strip()))

for _ in range(pair_num - 1):
    temp = pairs.get() + pairs.get()
    result += temp
    pairs.put(temp)

print(result)
