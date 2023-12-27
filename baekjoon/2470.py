import sys

sol = int(sys.stdin.readline().strip())


def solve(left, right):
    global ans, result
    while left < right:
        left_sol = sols[left]
        right_sol = sols[right]

        temp = left_sol + right_sol

        if abs(temp) < ans:
            ans = abs(temp)
            result = [left_sol, right_sol]
            if ans == 0:
                break
        if temp < 0:
            left += 1
        else:
            right -= 1


if __name__ == '__main__':
    sols = list(map(int, sys.stdin.readline().strip().split()))
    sols.sort()

    ans = abs(sols[0] + sols[-1])
    result = [sols[0], sols[-1]]

    solve(0, len(sols) - 1)

    print(result[0], result[1])