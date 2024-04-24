import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))

    NGE = [-1] * N
    st = [0]

    for i in range(1, N):
        while st and A[st[-1]] < A[i]:
            NGE[st.pop()] = A[i]
        st.append(i)

    print(*NGE)
