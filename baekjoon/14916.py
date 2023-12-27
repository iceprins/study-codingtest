import sys

if __name__ == '__main__':
    change = int(sys.stdin.readline())

    coin_num = change // 5
    remain = change % 5

    while coin_num != 0 or remain % 2 == 0:
        if remain % 2 != 0:
            coin_num -= 1
            remain += 5
        else:
            coin_num += remain // 2
            remain = 0
            break

    if remain != 0:
        print(-1)
    else:
        print(coin_num)