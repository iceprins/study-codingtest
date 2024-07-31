def solution(storey):
    answer = 0

    while storey:
        remainder = storey % 10
        if (remainder == 5 and storey // 10 % 10 >= 5) or remainder > 5:
            storey += 10 - remainder
            answer += 10 - remainder
        else:
            answer += remainder
        storey = storey // 10

    return answer
