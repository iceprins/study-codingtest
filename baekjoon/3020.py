import sys

if __name__ == '__main__':
    N, H = map(int, sys.stdin.readline().strip().split())
    lines = [0] * H

    for i in range(N):
        size = int(sys.stdin.readline().strip())
        if i % 2 == 0:
            lines[H - size] += 1
        else:
            lines[0] += 1
            lines[size] -= 1

    for i in range(1, H):
        lines[i] += lines[i - 1]

    result = 0
    low = min(lines)

    for l in lines:
        if l == low:
            result += 1

    print(low, result)
