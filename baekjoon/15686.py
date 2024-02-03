import sys
from itertools import combinations

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    city = list()
    chicken_pos = list()
    house_pos = list()
    ans = sys.maxsize

    for _ in range(N):
        city.append(list(map(int, sys.stdin.readline().strip().split())))

    for i in range(N):
        for j in range(N):
            if city[i][j] == 2:
                chicken_pos.append((i, j))
            if city[i][j] == 1:
                house_pos.append((i, j))

    cand = list(combinations(chicken_pos, M))

    for elem in cand:
        tmp = 0
        for house in house_pos:
            dist = sys.maxsize
            for i in range(M):
                dist = min(dist, abs(house[0] - elem[i][0]) + abs(house[1] - elem[i][1]))
            tmp += dist
        ans = min(ans, tmp)

    print(ans)
