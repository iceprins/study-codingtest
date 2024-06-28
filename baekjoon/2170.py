import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    pos = []

    for _ in range(N):
        x, y = map(int, sys.stdin.readline().strip().split())
        pos.append((x, y))

    pos.sort(key=lambda x: (x[0], x[1]), reverse=True)

    cal = []

    while pos:
        if not cal:
            cal.append(pos.pop())
            continue

        old_x, old_y = cal.pop()
        x, y = pos.pop()

        if x > old_y:
            cal.append((old_x, old_y))
            cal.append((x, y))
        elif old_x < x and old_y > y:
            cal.append((old_x, old_y))
        else:
            cal.append((old_x, y))

    ans = 0

    for elem in cal:
        ans += (elem[1] - elem[0])

    print(ans)
