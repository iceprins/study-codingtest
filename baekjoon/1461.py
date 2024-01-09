import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    position = list(map(int, sys.stdin.readline().strip().split()))

    positive_pos = list()
    negative_pos = list()

    for elem in position:
        if elem > 0:
            positive_pos.append(elem)
        else:
            negative_pos.append(-elem)

    positive_pos.sort(reverse=True)
    negative_pos.sort(reverse=True)

    positive_farthest = 0
    negative_farthest = 0

    if len(positive_pos) != 0:
        positive_farthest = max(positive_pos)

    if len(negative_pos) != 0:
        negative_farthest = max(negative_pos)

    farthest = max(positive_farthest, negative_farthest)
    result = 0

    for i in range(0, len(positive_pos), M):
        result += 2 * positive_pos[i]

    for i in range(0, len(negative_pos), M):
        result += 2 * negative_pos[i]

    result -= farthest

    print(result)