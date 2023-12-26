def sum_of_digit(n):
    s = 0
    for d in str(n):
        s += int(d)
    return s + n

if __name__ == '__main__':
    total = list(range(1, 10001))
    ans = list()

    while total:
        num = total[0]
        ans.append(num)
        total.remove(num)
        next_num = sum_of_digit(num)
        while next_num <= 10000:
            if next_num in total:
                total.remove(next_num)
                next_num = sum_of_digit(next_num)
            else:
                break

    print(ans)