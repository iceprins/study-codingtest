import sys


def search(left, right, target):
    if left > right:
        return 0

    mid = (left + right) // 2

    if cards[mid] == target:
        return count.get(target)
    elif cards[mid] < target:
        return search(mid + 1, right, target)
    else:
        return search(left, mid - 1, target)


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    cards = list(map(int, sys.stdin.readline().strip().split()))
    M = int(sys.stdin.readline().strip())
    targets = list(map(int, sys.stdin.readline().strip().split()))

    cards.sort()

    count = dict()
    for card in cards:
        if card in count:
            count[card] += 1
        else:
            count[card] = 1

    ans = list()

    for target in targets:
        ans.append(search(0, N - 1, target))

    print(*ans)
