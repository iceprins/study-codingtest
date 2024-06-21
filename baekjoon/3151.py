import sys
from bisect import bisect_left

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    skill = sorted(list(map(int, sys.stdin.readline().strip().split())))

    ans = 0

    for i in range(len(skill) - 2):
        left, right = i + 1, N - 1
        while left < right:
            result = skill[i] + skill[left] + skill[right]
            if result > 0:
                right -= 1
            else:
                if result == 0:
                    if skill[left] == skill[right]:
                        ans += right - left
                    else:
                        idx = bisect_left(skill, skill[right])
                        ans += right - idx + 1
                left += 1

    print(ans)
