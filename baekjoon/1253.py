import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split()))

    nums.sort()
    cnt = 0

    for i in range(N):
        target = nums[i]
        start = 0
        end = N - 1
        while start < end:
            if nums[start] + nums[end] == target:
                if start == i:
                    start += 1
                elif end == i:
                    end -= 1
                else:
                    cnt += 1
                    break
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                start += 1

    print(cnt)
