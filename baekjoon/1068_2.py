import sys


def dfs(node, arr):
    arr[node] = -2
    for i in range(len(arr)):
        if node == arr[i]:
            dfs(i, arr)


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    parents = list(map(int, sys.stdin.readline().strip().split()))
    target = int(sys.stdin.readline().strip())

    dfs(target, parents)

    cnt = 0
    for i in range(len(parents)):
        if parents[i] != -2 and i not in parents:
            cnt += 1

    print(cnt)
