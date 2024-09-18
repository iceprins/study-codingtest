# 단순 구현 풀이
def solution(numbers):
    answer = [-1] * len(numbers)
    
    for i in range(len(numbers) - 1, 0, -1):
        num = numbers[i]
        for j in range(i - 1, -1, -1):
            if numbers[j] >= num:
                break
            answer[j] = num

    return answer


# Stack 풀이
def solution(numbers):
    answer = [-1] * len(numbers)
    st = []

    for i in range(len(numbers)):
        while st and numbers[st[-1]] < numbers[i]:
            answer[st.pop()] = numbers[i]
        st.append(i)

    return answer
