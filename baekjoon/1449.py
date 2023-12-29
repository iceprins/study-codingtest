import sys

if __name__ == '__main__':
    N, L = map(int, sys.stdin.readline().strip().split())
    hole = list(map(int, sys.stdin.readline().strip().split()))

    hole.sort()

    limit = hole[0] + L - 1
    cnt = 1

    for elem in hole:
        if elem <= limit:
            continue
        cnt += 1
        limit = elem + L - 1

    print(cnt)