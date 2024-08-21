import sys, bisect

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))
    m = int(sys.stdin.readline().strip())
    B = list(map(int, sys.stdin.readline().strip().split()))

    a_A = []
    a_B = []

    for i in range(n):
        for j in range(i, n):
            a_A.append(sum(A[i:j + 1]))

    for i in range(m):
        for j in range(i, m):
            a_B.append(sum(B[i:j + 1]))

    a_A.sort()
    a_B.sort()

    ans = 0

    for i in range(len(a_A)):
        rest = T - a_A[i]
        left = bisect.bisect_left(a_B, rest)
        right = bisect.bisect_right(a_B, rest)
        ans += (right - left)

    print(ans)
