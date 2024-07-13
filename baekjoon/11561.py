import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        start, end = 1, N
        ans = 0

        while start <= end:
            mid = (start + end) // 2
            result = (mid * (mid + 1)) // 2

            if result > N:
                end = mid - 1
            else:
                start = mid + 1
                ans = mid

        print(ans)
