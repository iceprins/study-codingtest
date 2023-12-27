import sys


def search(start, end):
    while start <= end:
        mid = (start + end) // 2
        if mid ** 2 >= input_val:
            end = mid - 1
        else:
            start = mid + 1

    return start


if __name__ == '__main__':
    input_val = int(sys.stdin.readline().strip())

    print(search(0, input_val))