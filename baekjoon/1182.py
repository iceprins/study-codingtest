import sys


def dfs(idx, value):
    if idx == N:
        if value == S:
            result.append(1)
        return

    dfs(idx + 1, value + sequence[idx + 1])
    dfs(idx + 1, value)


if __name__ == '__main__':
    N, S = map(int, sys.stdin.readline().strip().split())
    sequence = list(map(int, sys.stdin.readline().strip().split()))
    sequence.insert(0, 0)
    result = list()

    dfs(0, 0)

    print(len(result) - 1 if S == 0 else len(result))
