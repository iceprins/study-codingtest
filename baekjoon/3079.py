import sys


N, M = map(int, sys.stdin.readline().strip().split())
T = list()

for _ in range(N):
    T.append(int(sys.stdin.readline().strip()))


def bin_search(start, end):
    global ans
    while start <= end:
        tot = 0
        mid = (start + end) // 2

        for i in range(N):
            tot += mid // T[i]

        if tot >= M:
            end = mid - 1
            ans = min(mid, ans)
        else:
            start = mid + 1

    return ans


if __name__ == '__main__':
    left = min(T)
    right = max(T) * M
    ans = right

    print(bin_search(left, right))