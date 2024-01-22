import sys


def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                bus_info[i][j] = min(bus_info[i][j], bus_info[i][k] + bus_info[k][j])


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    bus_info = [[sys.maxsize for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        bus_info[a - 1][b - 1] = min(bus_info[a - 1][b - 1], c)

    for i in range(n):
        bus_info[i][i] = 0

    floyd()

    for i in range(n):
        for j in range(n):
            if bus_info[i][j] == sys.maxsize:
                bus_info[i][j] = 0

    for row in bus_info:
        print(*row)
