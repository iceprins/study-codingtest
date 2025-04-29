import math


def solution(numbers):
    answer = 0

    numbers = list(numbers)
    cand = set()
    n = len(numbers)

    def dfs(arr, valid, number):
        if len(valid) == n:
            cand.add(int(number))
            return
        if number != "":
            cand.add(int(number))
        for i in range(len(arr)):
            if i not in valid:
                valid.append(i)
                dfs(arr, valid, number + arr[i])
                valid.pop()

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    dfs(list(numbers), [], "")

    for x in cand:
        if is_prime(x):
            answer += 1

    return answer
