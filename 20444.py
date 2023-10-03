import sys

n, k = map(int, sys.stdin.readline().strip().split())


def search(start, end):
    while start <= end:
        mid = (start + end) // 2
        piece = (mid + 1) * (n - mid + 1)
        if piece == k:
            return "YES"
        if piece > k:
            end = mid - 1
        else:
            start = mid + 1
    return "NO"


if __name__ == '__main__':
    print(search(0, n // 2))