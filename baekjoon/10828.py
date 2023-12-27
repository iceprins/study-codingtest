import sys

if __name__ == '__main__':
    stack = list()
    N = int(sys.stdin.readline().strip())

    for _ in range(N):
        input_line = list(sys.stdin.readline().strip().split(" "))
        instruction = input_line[0]

        if instruction == 'push':
            stack.append(input_line[1])
            continue
        elif instruction == 'pop':
            if len(stack) == 0:
                print("-1")
                continue
            print(stack.pop())
            continue
        elif instruction == 'size':
            print(len(stack))
            continue
        elif instruction == 'empty':
            if len(stack) == 0:
                print("1")
                continue
            print("0")
            continue
        elif instruction == 'top':
            if len(stack) == 0:
                print("-1")
                continue
            print(stack[-1])
            continue