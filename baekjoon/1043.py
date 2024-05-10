# set 풀이
import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    true = set(list(map(int, sys.stdin.readline().strip().split()))[1:])
    parties = []

    for _ in range(M):
        party = set(list(map(int, sys.stdin.readline().strip().split()))[1:])
        parties.append(party)

    for _ in range(M):
        for party in parties:
            if len(party.intersection(true)):
                true = true.union(party)

    ans = 0

    for party in parties:
        if len(party.intersection(true)) == 0:
            ans += 1

    print(ans)


# union-find 풀이
import sys


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x in true and y in true:
        return

    if x in true:
        parents[y] = x
    elif y in true:
        parents[x] = y
    else:
        if x < y:
            parents[y] = x
        else:
            parents[x] = y


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    true = list(map(int, sys.stdin.readline().strip().split()))[1:]
    parties = []
    parents = [i for i in range(N + 1)]

    for _ in range(M):
        party = list(map(int, sys.stdin.readline().strip().split()))
        party_len = party[0]
        party = party[1:]

        for i in range(party_len - 1):
            union(party[i], party[i + 1])

        parties.append(party)

    ans = 0

    for party in parties:
        for i in range(len(party)):
            if find(party[i]) in true:
                break
        else:
            ans += 1

    print(ans)
