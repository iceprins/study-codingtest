import math


def solution(progresses, speeds):
    ans = []
    extra = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    idx = 0

    for i in range(len(extra)):
        if extra[idx] < extra[i]:
            ans.append(i - idx)
            idx = i

    ans.append(len(extra) - idx)

    return ans
