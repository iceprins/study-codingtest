import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())

    weight = list()
    ans = list()

    for _ in range(N):
        weight.append(int(sys.stdin.readline().strip()))
    weight.sort(reverse=True)

    for i in range(N):
        ans.append((i + 1) * weight[i])

    print(max(ans))