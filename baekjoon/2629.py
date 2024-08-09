import sys


def calculate(num, weight):
    if num > weight_num:
        return
    if dp[num][weight] == 1:
        return
    dp[num][weight] = 1

    calculate(num + 1, weight + weights[num - 1])
    calculate(num + 1, weight)
    calculate(num + 1, abs(weight - weights[num - 1]))


if __name__ == '__main__':
    weight_num = int(sys.stdin.readline().strip())
    weights = list(map(int, sys.stdin.readline().strip().split()))
    bead_num = int(sys.stdin.readline().strip())
    beads = list(map(int, sys.stdin.readline().strip().split()))

    dp = [[0 for _ in range((500 * j) + 1)] for j in range(weight_num + 1)]

    calculate(0, 0)

    ans = []

    for bead in beads:
        if bead > 500 * weight_num:
            ans.append("N")
        elif dp[weight_num][bead] == 1:
            ans.append("Y")
        else:
            ans.append("N")

    print(*ans)
