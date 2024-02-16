import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    seq = list(map(int, sys.stdin.readline().strip().split()))
    reverse_seq = list(reversed(seq))

    dp_increase = [1] * N
    dp_decrease = [1] * N

    for i in range(N):
        for j in range(i):
            if seq[i] > seq[j]:
                dp_increase[i] = max(dp_increase[i], dp_increase[j] + 1)
            if reverse_seq[i] > reverse_seq[j]:
                dp_decrease[i] = max(dp_decrease[i], dp_decrease[j] + 1)

    result = [0] * N
    for i in range(N):
        result[i] = dp_increase[i] + dp_decrease[N - i - 1] - 1

    print(max(result))
