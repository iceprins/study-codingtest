import sys

bulb, order = map(int, sys.stdin.readline().strip().split())
bulb_cond = list(map(int, sys.stdin.readline().strip().split()))


def change_condition(n, info1, info2):
    if n == 1:
        bulb_cond[info1 - 1] = info2
    elif n == 2:
        for i in range(info1 - 1, info2):
            bulb_cond[i] = (bulb_cond[i] - 1) ** 2
    elif n == 3:
        for i in range(info1 - 1, info2):
            bulb_cond[i] = 0
    else:
        for i in range(info1 - 1, info2):
            bulb_cond[i] = 1


def print_cond(input_list):
    for i in range(len(input_list)):
        print(input_list[i], end=' ')


if __name__ == '__main__':
    for _ in range(order):
        order_num, order_info_1, order_info_2 = map(int, sys.stdin.readline().strip().split())
        change_condition(order_num, order_info_1, order_info_2)

    print_cond(bulb_cond)