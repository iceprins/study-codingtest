import sys


def binary_search(start, end):
    global ans
    while start <= end:
        mid = (start + end) // 2
        if mid * (mid + 1) // 2 <= S:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans


if __name__ == '__main__':
    S = int(sys.stdin.readline().strip())
    ans = 0
    result = binary_search(1, S)

    print(result)