import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    K = int(sys.stdin.readline().strip())
    sensors = list(map(int, sys.stdin.readline().strip().split()))
    dist = list()

    sensors.sort()

    for i in range(1, N):
        dist.append(sensors[i] - sensors[i - 1])

    dist.sort()

    ans = 0
    for i in range(N - K):
        ans += dist[i]

    print(ans)
