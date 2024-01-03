import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        applicants = list()
        for _ in range(N):
            applicants.append(tuple(map(int, sys.stdin.readline().strip().split())))

        applicants.sort(reverse=True, key=lambda x: x[1])
        applicants.sort(key=lambda x:x[0])

        cnt = 1
        std_score = applicants[0][1]

        for i in range(1, N):
            if applicants[i][1] <= std_score:
                cnt += 1
                std_score = applicants[i][1]

        print(cnt)