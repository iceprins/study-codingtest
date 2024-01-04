import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    K = int(sys.stdin.readline().strip())
    sensor_loc = list(map(int, sys.stdin.readline().strip().split()))

    sensor_loc.sort()

    distance = list()
    ans = 0

    for i in range(N - 1):
        distance.append(sensor_loc[i + 1] - sensor_loc[i])

    distance.sort(reverse=True)

    for i in range(min(K - 1, N - 1)):
        ans += distance[i]

    print(sum(distance) - ans)