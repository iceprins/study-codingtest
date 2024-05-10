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
