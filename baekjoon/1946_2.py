import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        scores = list(tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N))

        scores.sort(key=lambda x: x[0])

        cnt = 1
        std_score = scores[0][1]

        for i in range(1, N):
            if std_score >= scores[i][1]:
                cnt += 1
                std_score = scores[i][1]

        print(cnt)
