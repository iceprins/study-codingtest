import sys


def calculate(a, b, op):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b


def dfs(idx, value):
    global result

    if idx == N - 1:
        result = max(result, value)
        return

    if idx + 2 < N:
        next_value = calculate(value, int(expression[idx + 2]), expression[idx + 1])
        dfs(idx + 2, next_value)

    if idx + 4 < N:
        next_next_value = calculate(int(expression[idx + 2]), int(expression[idx + 4]), expression[idx + 3])
        next_value = calculate(value, next_next_value, expression[idx + 1])
        dfs(idx + 4, next_value)


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    expression = list(sys.stdin.readline().strip())
    result = -sys.maxsize

    dfs(0, int(expression[0]))
    print(result)
