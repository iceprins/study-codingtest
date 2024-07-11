import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        N, M = map(int, sys.stdin.readline().strip().split())
        A = list(map(int, sys.stdin.readline().strip().split()))
        B = list(map(int, sys.stdin.readline().strip().split()))

        A.sort()
        B.sort()

        cnt = 0

        for i in range(N):
            start, end = 0, M - 1
            tmp = 0

            while start <= end:
                mid = (start + end) // 2
                if B[mid] < A[i]:
                    start = mid + 1
                    tmp = mid + 1
                else:
                    end = mid - 1

            cnt += tmp

        print(cnt)
