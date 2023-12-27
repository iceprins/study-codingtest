import sys

if __name__ == '__main__':
    sport_goods = int(sys.stdin.readline().strip())
    loss = list(map(int, sys.stdin.readline().strip().split()))
    loss.sort()

    temp = list()
    max_val = 0
    if sport_goods % 2 == 0:
        for i in range(sport_goods//2):
            temp.append(loss[i] + loss[sport_goods - 1 - i])
    else:
        for i in range((sport_goods - 1)//2):
            temp.append(loss[i] + loss[sport_goods - 2 - i])
        temp.append(loss[-1])

    print(max(temp))