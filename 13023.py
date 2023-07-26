import sys


N, M = map(int, sys.stdin.readline().strip().split())
relationship = [[] for _ in range(N)]
visited = [False] * N
is_exist = 0

for _ in range(M):
    me, friend = map(int, sys.stdin.readline().strip().split())
    relationship[me].append(friend)
    relationship[me].sort()
    if me not in relationship[friend]:
        relationship[friend].append(me)
        relationship[friend].sort()


def dfs(v, length):
    global is_exist
    visited[v] = True
    if length == 4:
        is_exist = 1
        print(1)
        sys.exit(0)
    for i in relationship[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i, length + 1)
            visited[i] = False


if __name__ == '__main__':
    for i in range(N):
        dfs(i, 0)
        visited[i] = False

    print(is_exist)