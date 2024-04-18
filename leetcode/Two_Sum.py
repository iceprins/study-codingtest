class Solution(object):
    def twoSum(self, nums, target):
        table = {}

        for i, num in enumerate(nums):
            rest = target - num
            if rest in table:
                return [i, table[rest]]
            else:
                table[num] = i
