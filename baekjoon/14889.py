import sys
from itertools import combinations

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    S = list()

    for _ in range(N):
        S.append(list(map(int, sys.stdin.readline().strip().split())))

    total = list(combinations(tuple(i for i in range(1, N + 1)), N // 2))
    scores = list()

    for i in range(len(total)):
        start = 0
        link = 0

        start_team = total[i]
        link_team = tuple(set(i for i in range(1, N + 1)) - set(start_team))

        start_pairs = list(combinations(start_team, 2))
        link_pairs = list(combinations(link_team, 2))

        for j in range(len(start_pairs)):
            start += S[start_pairs[j][0] - 1][start_pairs[j][1] - 1]
            start += S[start_pairs[j][1] - 1][start_pairs[j][0] - 1]
            link += S[link_pairs[j][0] - 1][link_pairs[j][1] - 1]
            link += S[link_pairs[j][1] - 1][link_pairs[j][0] - 1]

        scores.append(abs(start - link))

    print(min(scores))
