if __name__ == '__main__':
    X, Y = map(int, input().split())
    Z = int(Y * 100 / X)

    start, end = 1, X
    ans = -1

    while start <= end:
        mid = (start + end) // 2
        tmp = int((Y + mid) * 100 / (X + mid))
        if tmp == Z:
            start = mid + 1
        else:
            ans = mid
            end = mid - 1

    print(ans)
