import sys

if __name__ == '__main__':
    digit, erase = map(int, sys.stdin.readline().strip().split())
    number = list(sys.stdin.readline().strip())
    copy = erase

    temp = list()

    for i in range(digit):
        while erase > 0 and temp:
            if temp[-1] < number[i]:
                temp.pop()
                erase -= 1
            else:
                break
        temp.append(number[i])

    print(*temp[:(digit - copy)], sep='')