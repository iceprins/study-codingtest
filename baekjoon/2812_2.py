import sys

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().strip().split())
    num = list(map(int, sys.stdin.readline().strip()))
    stack = list()

    for elem in num:
        while stack and stack[-1] < elem and K != 0:
            stack.pop()
            K -= 1
        stack.append(elem)

    ans = ""

    if K > 0:
        ans = ''.join(map(str, stack[:-K]))
    else:
        ans = ''.join(map(str, stack))

    print(ans)
