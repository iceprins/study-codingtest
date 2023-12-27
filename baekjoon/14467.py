import sys

if __name__ == '__main__':
    observe = int(sys.stdin.readline().strip())
    check = [-1] * 11
    result = 0

    for _ in range(observe):
        cow_num, cow_pos = map(int, sys.stdin.readline().strip().split())
        if check[cow_num] == -1:
            check[cow_num] = cow_pos
        elif check[cow_num] != cow_pos:
            check[cow_num] = cow_pos
            result += 1

    print(result)