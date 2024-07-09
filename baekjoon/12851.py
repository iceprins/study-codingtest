from collections import deque


def bfs(x):
    q = deque()
    q.append(x)
    global result, cnt

    while q:
        now = q.popleft()
        tmp = visited[now]
        if now == K:
            result = tmp
            cnt += 1
            continue

        for i in (now - 1, now + 1, 2 * now):
            if 0 <= i < 100001 and (visited[i] == 0 or visited[i] == visited[now] + 1):
                visited[i] = visited[now] + 1
                q.append(i)


if __name__ == '__main__':
    N, K = map(int, input().split())
    visited = [0] * 100001
    result, cnt = 0, 0

    bfs(N)

    print(result)
    print(cnt)
