import sys
from collections import deque


def D(n):
    return (2 * n) % 10000


def S(n):
    return (n - 1) % 10000


def L(n):
    return n // 1000 + (n % 1000) * 10


def R(n):
    return (n % 10) * 1000 + n // 10


def bfs(n):
    q = deque()
    q.append([n, ''])
    visited[n] = True

    while q:
        num, command = q.popleft()

        if num == B:
            print(command)
            break

        d = D(num)
        if not visited[d]:
            visited[d] = True
            q.append([d, command + 'D'])

        s = S(num)
        if not visited[s]:
            visited[s] = True
            q.append([s, command + 'S'])

        l = L(num)
        if not visited[l]:
            visited[l] = True
            q.append([l, command + 'L'])

        r = R(num)
        if not visited[r]:
            visited[r] = True
            q.append([r, command + 'R'])


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        A, B = map(int, sys.stdin.readline().strip().split())

        visited = [False] * 10000

        bfs(A)
