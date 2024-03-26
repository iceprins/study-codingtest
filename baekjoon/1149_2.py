import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    costs = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

    for i in range(1, N):
        costs[i][0] = min(costs[i - 1][1], costs[i - 1][2]) + costs[i][0]
        costs[i][1] = min(costs[i - 1][0], costs[i - 1][2]) + costs[i][1]
        costs[i][2] = min(costs[i - 1][0], costs[i - 1][1]) + costs[i][2]

    print(min(costs[N - 1]))
