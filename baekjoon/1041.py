import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    num = list(map(int, sys.stdin.readline().strip().split()))
    used_num = [min(num[0], num[5]), min(num[1], num[4]), min(num[2], num[3])]
    used_num.sort()

    sum_of_three = sum(used_num)
    sum_of_two = sum_of_three - used_num[2]

    ans = 0

    if N == 1:
        ans = sum(num) - max(num)
    else:
        ans = 4 * sum_of_three + 4 * (2 * N - 3) * sum_of_two + (N - 2) * (5 * N - 6) * used_num[0]

    print(ans)