import sys


def check(a, b, op):
    if op == '<':
        if a > b:
            return False
    if op == '>':
        if a < b:
            return False
    return True


def dfs(cnt, num):
    if cnt == k + 1:
        result.append(num)
        return

    for i in range(10):
        if visited[i]:
            continue
        if cnt == 0 or check(num[cnt - 1], str(i), sign[cnt - 1]):
            visited[i] = True
            dfs(cnt + 1, num + str(i))
            visited[i] = False


if __name__ == '__main__':
    k = int(sys.stdin.readline().strip())
    sign = list(sys.stdin.readline().strip().split())
    result = list()
    visited = [False] * 10
    nums = [i for i in range(10)]

    dfs(0, '')
    result.sort()

    print(result[-1])
    print(result[0])
