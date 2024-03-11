from collections import deque


def bfs(vertex):
    q = deque()
    q.append(vertex)
    cnt = 0
    while q:
        now = q.popleft()
        if now == K:
            return visited[now]
        for i in (now - 1, now + 1, now * 2):
            if 0 <= i <= 100000 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[now] + 1
                cnt += 1


if __name__ == '__main__':
    N, K = map(int, input().split())
    visited = [0] * 100001

    print(bfs(N))
