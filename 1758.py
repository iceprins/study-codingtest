import sys

if __name__ == '__main__':
    waiting = int(sys.stdin.readline().strip())
    tips = list()

    for _ in range(waiting):
        tips.append(int(sys.stdin.readline().strip()))

    tips.sort(reverse=True)
    tip_sum = 0

    for i in range(waiting):
        allowed_tip = tips[i] - i
        if allowed_tip >= 0:
            tip_sum += allowed_tip

    print(tip_sum)
