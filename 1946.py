import sys

case_num = int(sys.stdin.readline().strip())

for _ in range(case_num):
    A = list()
    result = 1
    cand_num = int(sys.stdin.readline().strip())
    for _ in range(cand_num):
        paper_score, interview_score = map(int, sys.stdin.readline().split())
        A.append((paper_score, interview_score))

    A.sort(key=lambda x: x[0])

    temp = A[0][1]

    for i in range(1, cand_num):
        if A[i][1] < temp:
            result += 1
            temp = A[i][1]

    print(result)
