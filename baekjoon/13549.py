from collections import deque


def bfs(s, v, h):
    queue = deque()
    queue.append(s)
    v[s] = True

    while queue:
        now = queue.popleft()
        if now == K:
            return h[now]
        for new in (2 * now, now - 1, now + 1):
            if new < 0 or new > 100000:
                continue
            if not v[new]:
                v[new] = True
                queue.append(new)
                if new == 2 * now:
                    h[new] = h[now]
                else:
                    h[new] = h[now] + 1


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    visited = [False] * 100001
    history = [0] * 100001

    print(bfs(N, visited, history))