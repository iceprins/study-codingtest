import sys

if __name__ == '__main__':
    basic = sys.stdin.readline().strip()
    explode = sys.stdin.readline().strip()

    stack = []

    for i in range(len(basic)):
        stack.append(basic[i])
        if "".join(stack[-len(explode):]) == explode:
            for _ in range(len(explode)):
                stack.pop()

    if stack:
        print("".join(stack))
    else:
        print("FRULA")
