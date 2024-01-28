def make_self_number(n):
    return n + sum(list(map(int, str(n))))


if __name__ == '__main__':
    nums = [i for i in range(1, 10001)]

    normal_nums = list()

    for num in nums:
        self_number = make_self_number(num)
        if self_number <= 10000:
            normal_nums.append(make_self_number(num))

    self_numbers = list(set(nums) - set(normal_nums))
    self_numbers.sort()

    for elem in self_numbers:
        print(elem)
