def solution(answers):
    answer = []

    first_ans = [1, 2, 3, 4, 5]
    second_ans = [2, 1, 2, 3, 2, 4, 2, 5]
    third_ans = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0] * 3

    for i in range(len(answers)):
        if answers[i] == first_ans[i % 5]:
            scores[0] += 1
        if answers[i] == second_ans[i % 8]:
            scores[1] += 1
        if answers[i] == third_ans[i % 10]:
            scores[2] += 1

    max_score = max(scores)

    for i in range(3):
        if scores[i] == max_score:
            answer.append(i + 1)

    return answer
