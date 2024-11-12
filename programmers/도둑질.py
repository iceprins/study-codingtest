def solution(money):
    dp1 = [0] * len(money)

    for i in range(len(money) - 1):
        if i == 0:
            dp1[i] = money[i]
        elif i == 1:
            dp1[i] = max(money[i], money[i - 1])
        else:
            dp1[i] = max(dp1[i - 1], money[i] + dp1[i - 2])

    dp2 = [0] * len(money)

    for i in range(1, len(money)):
        if i == 1:
            dp2[i] = money[i]
        elif i == 2:
            dp2[i] = max(money[i], money[i - 1])
        else:
            dp2[i] = max(dp2[i - 1], money[i] + dp2[i - 2])

    return max(max(dp1), max(dp2))
