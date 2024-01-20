import sys

if __name__ == '__main__':
    S = list(sys.stdin.readline().strip())
    T = list(sys.stdin.readline().strip())

    for i in range(len(T) - len(S)):
        temp = T.pop()
        if temp == 'B':
            T.reverse()

    if S == T:
        print(1)
    else:
        print(0)
