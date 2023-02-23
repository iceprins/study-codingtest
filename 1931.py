import sys

meeting_num = int(sys.stdin.readline())

time_pairs = list()
for _ in range(meeting_num):
    pairs = sys.stdin.readline().strip()
    start_time = int(pairs.split()[0])
    end_time = int(pairs.split()[1])
    time_pairs.append((start_time, end_time))

time_pairs = sorted(time_pairs, key=lambda a: a[0])
time_pairs = sorted(time_pairs, key=lambda a: a[1])

last = 0
result = 0

for time in time_pairs:
    if time[0] >= last:
        result += 1
        last = time[1]

print(result)