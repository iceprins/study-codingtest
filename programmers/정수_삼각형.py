# 240219 풀이
def solution(triangle):
    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i + 1])):
            if i == 0:
                triangle[1][j] += triangle[0][0]
            else:
                if j == 0:
                    triangle[i + 1][0] += triangle[i][0]
                elif j == len(triangle[i + 1]) - 1:
                    triangle[i + 1][j] += triangle[i][len(triangle[i]) - 1]
                else:
                    triangle[i + 1][j] = max(triangle[i + 1][j] + triangle[i][j - 1],
                                             triangle[i + 1][j] + triangle[i][j])

    answer = max(triangle[-1])

    return answer


# 241128 풀이
def solution(triangle):
    for i in range(len(triangle) - 1, 0, -1):
        for j in range(len(triangle[i]) - 1):
            triangle[i - 1][j] += max(triangle[i][j], triangle[i][j + 1])

    return triangle[0][0]
