# Prim 알고리즘 풀이
import sys
import heapq


def prim(start):
    heap = []
    selected = [False] * (N + 1)

    heapq.heappush(heap, (0, start))
    ans = 0

    while heap:
        cost, vertex = heapq.heappop(heap)
        if not selected[vertex]:
            selected[vertex] = True
            ans += cost
            for i in range(1, N + 1):
                # 연결이 되어 있고 아직 포함되지 않았다면
                if graph[vertex][i] != 0 and not selected[i]:
                    heapq.heappush(heap, (graph[vertex][i], i))

    return ans


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())
    parents = [i for i in range(N + 1)]

    graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        graph[a][b] = graph[b][a] = c

    print(prim(1))


# Kruskal 동작 방식
import sys


def find(x):
    # parents[x]가 x의 부모가 아니라면
    if parents[x] != x:
        # parents[x]를 기존 parents[x]의 부모로 업데이트
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def kruskal():
    ans = 0

    for connect in connects:
        cost, a, b = connect
        if find(a) != find(b):
            union(a, b)
            ans += cost

    return ans


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())
    parents = [i for i in range(N + 1)]

    connects = []

    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        connects.append((c, a, b))

    connects.sort()

    print(kruskal())
