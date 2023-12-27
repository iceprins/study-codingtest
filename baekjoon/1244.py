import sys

switch = int(sys.stdin.readline().strip())
switch_cond = list(map(int, sys.stdin.readline().strip().split()))


def change_cond(sex_info, num_info):
    if sex_info == 1:
        for i in range(switch):
            if (i+1) % num_info == 0:
                 switch_cond[i] = 1 - switch_cond[i]
    else:
        for i in range(min(num_info, switch - num_info + 1)):
            if switch_cond[num_info + i - 1] == switch_cond[num_info - i - 1] and i != 0:
                switch_cond[num_info + i - 1] = 1 - switch_cond[num_info + i - 1]
                switch_cond[num_info - i - 1] = 1 - switch_cond[num_info - i - 1]
            elif i == 0:
                switch_cond[num_info - 1] = 1 - switch_cond[num_info - 1]
            else:
                break


def print_cond(input_list):
    for i in range(len(input_list)):
        print(input_list[i], end=' ')
        if (i + 1) % 20 == 0:
            print()


if __name__ == '__main__':
    student = int(sys.stdin.readline().strip())

    for _ in range(student):
        sex, num = map(int, sys.stdin.readline().strip().split())
        change_cond(sex, num)

    print_cond(switch_cond)