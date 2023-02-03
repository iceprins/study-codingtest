import sys

people_num = int(sys.stdin.readline())

spend_time = list(map(int, sys.stdin.readline().split()))
spend_time.sort()

result = 0
for i in range(people_num):
    result += spend_time[i] * (people_num - i)

print(result)
