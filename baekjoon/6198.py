import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    H = [int(sys.stdin.readline().strip()) for _ in range(N)]

    st = []
    ans = 0

    for i in range(N):
        while st and st[-1] <= H[i]:
            st.pop()

        st.append(H[i])
        ans += len(st) - 1

    print(ans)
