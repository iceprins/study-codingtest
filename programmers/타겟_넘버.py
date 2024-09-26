def dfs(v, idx, result, numbers, target, ans):
    if idx == len(numbers):
        if result == target:
            ans += 1
        return ans
    v[idx] = True
    ans = dfs(v, idx + 1, result + numbers[idx], numbers, target, ans)
    ans = dfs(v, idx + 1, result - numbers[idx], numbers, target, ans)
    v[idx] = False

    return ans


def solution(numbers, target):
    visited = [False] * len(numbers)

    ans = dfs(visited, 0, 0, numbers, target, 0)

    return ans


# 240926 풀이
def solution(numbers, target):
    answer = 0

    def dfs(idx, s):
        nonlocal answer
        if idx == len(numbers):
            if s == target:
                answer += 1
            return

        dfs(idx + 1, s + numbers[idx])
        dfs(idx + 1, s - numbers[idx])

    dfs(0, 0)

    return answer
