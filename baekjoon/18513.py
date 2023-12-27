import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())
N_loc = list(map(int, sys.stdin.readline().strip().split()))
queue = deque()
visited = dict()

for elem in N_loc:
    queue.append(elem)
    visited[elem] = 0


def bfs():
    global K
    while queue:
        if K <= 0:
            break
        k = queue.popleft()
        for p in [k-1, k+1]:
            if p not in visited and K > 0:
                visited[p] = visited[k] + 1
                K -= 1
                queue.append(p)


if __name__ == '__main__':
    bfs()
    ans = 0
    for i, j in visited.items():
        ans += j
    print(ans)
