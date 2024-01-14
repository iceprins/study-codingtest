from collections import deque

def bfs(vertex):
    queue = deque()
    queue.append(vertex)
    while queue:
        now = queue.popleft()
        if now == K:
            return visited[now]
        for  i in (now - 1, now + 1, now * 2):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[now] + 1
                queue.append(i)

if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    visited = [0] * 100001

    print(bfs(N))