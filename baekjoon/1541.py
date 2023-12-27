import sys


if __name__ == '__main__':
    statement = list(sys.stdin.readline().strip().split("-"))
    result = 0

    for i in statement[0].split("+"):
        result += int(i)

    for i in statement[1:]:
        for j in i.split("+"):
            result -= int(j)

    print(result)