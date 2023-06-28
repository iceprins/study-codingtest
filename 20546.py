import sys


def bnp(m, s):
    s_num = 0
    for i in range(14):
        s_num += m // s[i]
        m = m % s[i]
    return m + s_num * s[13]


def timing(m, s):
    s_num = 0
    std = s[0]
    check = 0
    for i in range(1, 14):
        if s[i] > std and check >= 0:
            check += 1
            if 0 <= check < 3:
                std = s[i]
            elif check >= 3 and s_num != 0:
                m += s_num * s[i]
                s_num = 0
                std = s[i]
            else:
                std = s[i]
            continue
        elif s[i] > std and check < 0:
            check = 1
            std = s[i]
            continue
        elif s[i] < std and check <= 0:
            check -= 1
            if -3 < check <= 0:
                std = s[i]
            elif check <= -3:
                s_num += m // s[i]
                m = m % s[i]
                std = s[i]
            continue
        elif s[i] < std and check > 0:
            check = -1
            std = s[i]
        continue
    return m + s_num * s[13]


if __name__ == '__main__':
    money = int(sys.stdin.readline().strip())
    stock = list(map(int, sys.stdin.readline().strip().split()))

    if bnp(money, stock) > timing(money, stock):
        print("BNP")
    elif bnp(money, stock) < timing(money, stock):
        print("TIMING")
    else:
        print("SAMESAME")