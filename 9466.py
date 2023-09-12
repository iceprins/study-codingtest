import sys
sys.setrecursionlimit(1000000)

T = int(sys.stdin.readline().strip())


def dfs(v):
    global result
    check.append(v)
    visited[v] = True
    temp = choice[v]

    if visited[temp]:
        if temp in check:
            result += check[check.index(temp):]
        return
    else:
        dfs(temp)


if __name__ == '__main__':
    for _ in range(T):
        n = int(sys.stdin.readline().strip())
        visited = [True] + [False] * n
        choice = [0] + list(map(int, sys.stdin.readline().strip().split()))

        result = list()
        for i in range(1, n + 1):
            if not visited[i]:
                check = list()
                dfs(i)

        print(n - len(result))