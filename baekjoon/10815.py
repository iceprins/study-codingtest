import sys

N = int(sys.stdin.readline().strip())
my_card = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
check_card = list(map(int, sys.stdin.readline().strip().split()))


def search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if my_card[mid] == target:
            return True
        elif my_card[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

        return search(start, end, target)

    return False


if __name__ == '__main__':
    my_card.sort()
    for elem in check_card:
        result = search(0, len(my_card) - 1, elem)
        if result:
            print(1, end=' ')
        else:
            print(0, end=' ')