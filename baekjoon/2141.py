import sys

if __name__ == '__main__':
    village_num = int(input())
    village_info = list()
    cal = list()

    for _ in range(village_num):
        village_info.append(list(map(int, sys.stdin.readline().strip().split())))

    village_info.sort()

    dist_sum = 0
    left_man = 0
    right_man = 0
    for i in range(village_num):
        dist_sum += (village_info[i][0] - village_info[0][0]) * village_info[i][1]
        right_man += village_info[i][1]

    min_dist = dist_sum
    result = village_info[0][0]
    for i in range(1, village_num):
        left_man += village_info[i-1][1]
        right_man -= village_info[i-1][1]
        dist_sum += (village_info[i][0] - village_info[i-1][0]) * (left_man - right_man)

        if min_dist > dist_sum:
            min_dist = dist_sum
            result = village_info[i][0]
