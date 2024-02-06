def add_digit(digit, num):
    if digit == 1:
        result.append(num)
    else:
        for i in range(num % 10):
            add_digit(digit - 1, num * 10 + i)


def back(digit):
    for i in range(digit - 1, 10):
        add_digit(digit, i)


if __name__ == '__main__':
    N = int(input())
    result = list()

    for i in range(1, 11):
        back(i)

    if N >= len(result):
        print(-1)
    else:
        print(result[N])
