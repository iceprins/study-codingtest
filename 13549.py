import sys
from collections import deque


me, sister = map(int, sys.stdin.readline().strip().split())
max_dist = 100001
check = [False] * max_dist
dist = [-1] * max_dist
queue = deque()

queue.append(me)
check[me] = True
dist[me] = 0


def bfs():
    while queue:
        now = queue.popleft()
        if now == sister:
            print(dist[now])
            break
        if 0 <= now - 1 < max_dist and check[now - 1] == False:
            queue.append(now - 1)
            check[now - 1] = True
            dist[now - 1] = dist[now] + 1
        if 0 < now * 2 < max_dist and check[now * 2] == False:
            queue.appendleft(now * 2)
            check[now * 2] = True
            dist[now * 2] = dist[now]
        if 0 <= now + 1 < max_dist and check[now + 1] == False:
            queue.append(now + 1)
            check[now + 1] = True
            dist[now + 1] = dist[now] + 1


if __name__ == '__main__':
    bfs()