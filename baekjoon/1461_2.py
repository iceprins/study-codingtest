import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    position = list(map(int, sys.stdin.readline().strip().split()))
    pos = list()
    neg = list()
    history = list()

    for i in position:
        if i > 0:
            pos.append(i)
        else:
            neg.append(abs(i))

    pos.sort(reverse=True)
    neg.sort(reverse=True)

    for i in range(len(pos)):
        if i % M == 0:
            history.append(pos[i])
    for i in range(len(neg)):
        if i % M == 0:
            history.append(neg[i])

    history.sort()

    ans = 2 * sum(history) - history[-1]
    print(ans)
