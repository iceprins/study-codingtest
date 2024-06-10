import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    liquid = list(map(int, sys.stdin.readline().strip().split()))

    start = 0
    end = N - 1

    idx1, idx2 = -1, -1
    min_val = sys.maxsize

    while start < end:
        tmp = liquid[start] + liquid[end]
        if tmp == 0:
            idx1 = start
            idx2 = end
            break
        elif tmp < 0:
            if abs(tmp) < min_val:
                min_val = abs(tmp)
                idx1 = start
                idx2 = end
            start += 1
        else:
            if abs(tmp) < min_val:
                min_val = abs(tmp)
                idx1 = start
                idx2 = end
            end -= 1

    print(liquid[idx1], liquid[idx2])
