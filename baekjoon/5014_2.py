from collections import deque


def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        now = q.popleft()
        for pos in (now + U, now - D):
            if pos < 1 or pos > F:
                continue
            if visited[pos] == 0:
                visited[pos] = visited[now] + 1
                q.append(pos)


if __name__ == '__main__':
    F, S, G, U, D = map(int, input().split())
    visited = [0] * (F + 1)

    bfs(S)

    if visited[G] == 0:
        print("use the stairs")
    else:
        print(visited[G] - 1)
