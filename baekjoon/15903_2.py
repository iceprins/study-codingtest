import sys
import heapq

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().strip().split())
    nums = list(map(int, sys.stdin.readline().strip().split()))

    nums.sort()

    for _ in range(m):
        first = heapq.heappop(nums)
        second = heapq.heappop(nums)
        heapq.heappush(nums, first + second)
        heapq.heappush(nums, first + second)

    print(sum(nums))
