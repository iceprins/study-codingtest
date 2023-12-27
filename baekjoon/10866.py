import sys

if __name__ == '__main__':
    deque = list()
    N = int(sys.stdin.readline().strip())

    for _ in range(N):
        input_line = list(sys.stdin.readline().strip().split(" "))
        instruction = input_line[0]

        if instruction == 'push_front':
            deque.insert(0, input_line[1])
        elif instruction == 'push_back':
            deque.append(input_line[1])
        elif instruction == 'pop_front':
            if len(deque) == 0:
                print("-1")
                continue
            print(deque.pop(0))
        elif instruction == 'pop_back':
            if len(deque) == 0:
                print("-1")
                continue
            print(deque.pop())
        elif instruction == 'size':
            print(len(deque))
            continue
        elif instruction == 'empty':
            if len(deque) == 0:
                print("1")
                continue
            print("0")
        elif instruction == 'front':
            if len(deque) == 0:
                print("-1")
                continue
            print(deque[0])
        elif instruction == 'back':
            if len(deque) == 0:
                print("-1")
                continue
            print(deque[-1])