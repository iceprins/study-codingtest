def generate(n):
    return n + sum(list(map(int, str(n))))


if __name__ == '__main__':
    nums = set(i for i in range(1, 10001))
    generated_nums = set()

    for i in range(1, 10001):
        generated_nums.add(generate(i))

    for n in sorted(nums - generated_nums):
        print(n)
