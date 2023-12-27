import sys
from collections import Counter

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    num_list = list()
    for _ in range(N):
        num_list.append(int(sys.stdin.readline().strip()))

    size = len(num_list)
    print(round(sum(num_list) / size))
    print(sorted(num_list)[(size-1)//2])

    frequency = Counter(num_list)
    max_value = max(frequency.values())
    cand = list()
    for elem in frequency:
        if frequency[elem] == max_value:
            cand.append(elem)
    print(sorted(cand)[1] if len(cand) > 1 else cand[0])

    print(max(num_list) - min(num_list))