import sys

calendar = [0] * 366

if __name__ == '__main__':
    plan = int(sys.stdin.readline().strip())

    for _ in range(plan):
        start, end = map(int, sys.stdin.readline().strip().split())

        for i in range(start, end + 1):
            calendar[i] += 1

    result, count, max_val = 0, 0, 0
    for i in range(366):
        if calendar[i] == 0:
            result += count * max_val
            count, max_val = 0, 0
        else:
            count += 1
            max_val = max(max_val, calendar[i])

    result += count * max_val

    print(result)