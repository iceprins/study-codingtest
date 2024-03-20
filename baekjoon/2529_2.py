import sys


def dfs(depth, s):
    if depth == k + 1:
        ans.append(s)
        return
    for i in range(10):
        if not visited[i]:
            if depth == 0 or eval(s[-1] + sign[depth - 1] + str(i)):
                visited[i] = True
                dfs(depth + 1, s + str(i))
                visited[i] = False


if __name__ == '__main__':
    k = int(sys.stdin.readline().strip())
    sign = list(sys.stdin.readline().strip().split())
    visited = [False] * 10
    ans = []

    dfs(0, "")

    ans.sort()

    print(ans[-1])
    print(ans[0])
